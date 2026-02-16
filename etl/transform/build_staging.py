from pathlib import Path
import pandas as pd
from etl.utils.logging import get_logger

log = get_logger(__name__)


def load_staging(conn, data_paths: dict, truncate: bool = True) -> None:
    if truncate:
        conn.execute("DELETE FROM stg_customers")
        conn.execute("DELETE FROM stg_visits")
        conn.execute("DELETE FROM stg_events")
        conn.commit()

    mapping = {
        "stg_customers": data_paths["customers_csv"],
        "stg_visits": data_paths["visits_csv"],
        "stg_events": data_paths["events_csv"],
    }

    for table, rel_path in mapping.items():
        csv_path = Path(rel_path)
        df = pd.read_csv(csv_path)
        df.to_sql(table, conn, if_exists="append", index=False)
        log.info("Loaded %s rows into %s", len(df), table)
