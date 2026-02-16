from etl.utils.logging import get_logger

log = get_logger(__name__)


def run_basic_checks(conn) -> None:
    total = conn.execute("SELECT COUNT(*) FROM fact_event").fetchone()[0]
    if total == 0:
        raise ValueError("fact_event is empty")

    nulls = conn.execute(
        "SELECT COUNT(*) FROM fact_event WHERE customer_key IS NULL"
    ).fetchone()[0]
    if nulls != 0:
        raise ValueError("Null customer_key found in fact_event")

    log.info("Validation passed: fact_event rows=%s", total)
