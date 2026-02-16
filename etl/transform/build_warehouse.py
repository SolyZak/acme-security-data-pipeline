import pandas as pd
from etl.utils.logging import get_logger

log = get_logger(__name__)


def build_date_dimension(conn) -> None:
    row = conn.execute(
        "SELECT MIN(date(event_ts)), MAX(date(event_ts)) FROM stg_events"
    ).fetchone()
    if not row or row[0] is None or row[1] is None:
        log.info("No events found. Skipping dim_date build.")
        return

    start_date, end_date = row
    dates = pd.date_range(start=start_date, end=end_date, freq="D")
    df = pd.DataFrame(
        {
            "date_key": dates.strftime("%Y%m%d").astype(int),
            "full_date": dates.strftime("%Y-%m-%d"),
            "year": dates.year,
            "month": dates.month,
            "day": dates.day,
            "week_of_year": dates.isocalendar().week.astype(int),
        }
    )

    conn.execute("DELETE FROM dim_date")
    df.to_sql("dim_date", conn, if_exists="append", index=False)
    conn.commit()
    log.info("Built dim_date with %s rows", len(df))


def build_dimensions(conn) -> None:
    conn.execute("DELETE FROM dim_customer")
    conn.execute("DELETE FROM dim_location")
    conn.execute("DELETE FROM dim_device")

    conn.execute(
        """
        INSERT INTO dim_customer (customer_id, full_name, email, phone, country, city, start_date, end_date, is_current)
        SELECT DISTINCT customer_id, full_name, email, phone, country, city, date('now'), NULL, 1
        FROM stg_customers
        """
    )

    conn.execute(
        """
        INSERT INTO dim_location (country, city)
        SELECT DISTINCT country, city
        FROM stg_customers
        """
    )

    conn.execute(
        """
        INSERT INTO dim_device (device_type)
        SELECT DISTINCT device_type
        FROM stg_visits
        """
    )

    conn.commit()
    log.info("Built dimensions: customer, location, device")


def build_facts(conn) -> None:
    conn.execute("DELETE FROM fact_event")

    conn.execute(
        """
        INSERT INTO fact_event (
          event_id,
          date_key,
          customer_key,
          location_key,
          device_key,
          event_type,
          event_value,
          visit_id,
          event_ts
        )
        SELECT
          e.event_id,
          CAST(strftime('%Y%m%d', e.event_ts) AS INTEGER) AS date_key,
          c.customer_key,
          l.location_key,
          d.device_key,
          e.event_type,
          e.event_value,
          e.visit_id,
          e.event_ts
        FROM stg_events e
        JOIN dim_customer c ON e.customer_id = c.customer_id AND c.is_current = 1
        JOIN stg_customers sc ON sc.customer_id = e.customer_id
        JOIN dim_location l ON l.country = sc.country AND l.city = sc.city
        JOIN stg_visits v ON v.visit_id = e.visit_id
        JOIN dim_device d ON d.device_type = v.device_type
        """
    )

    conn.commit()
    log.info("Built fact_event")
