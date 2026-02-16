import argparse
from pathlib import Path

from etl.utils.db import get_conn, execute_sql_file, load_config, repo_root
from etl.transform.build_staging import load_staging
from etl.transform.build_warehouse import (
    build_date_dimension,
    build_dimensions,
    build_facts,
)
from etl.validation.checks import run_basic_checks
from etl.utils.logging import get_logger

log = get_logger(__name__)


def init_db(conn) -> None:
    root = repo_root()
    sql_paths = [
        root / "sql" / "staging" / "stg_customers.sql",
        root / "sql" / "staging" / "stg_visits.sql",
        root / "sql" / "staging" / "stg_events.sql",
        root / "sql" / "warehouse" / "dim_customer.sql",
        root / "sql" / "warehouse" / "dim_date.sql",
        root / "sql" / "warehouse" / "dim_location.sql",
        root / "sql" / "warehouse" / "dim_device.sql",
        root / "sql" / "warehouse" / "fact_event.sql",
    ]

    for p in sql_paths:
        execute_sql_file(conn, p)
    log.info("Initialized database schema")


def load_staging_data(conn) -> None:
    cfg = load_config()
    root = repo_root()
    data_paths = {
        k: str(root / v) for k, v in cfg["data"].items()
    }
    load_staging(conn, data_paths, truncate=True)


def build_warehouse(conn) -> None:
    build_date_dimension(conn)
    build_dimensions(conn)
    build_facts(conn)


def validate(conn) -> None:
    run_basic_checks(conn)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the demo data pipeline")
    parser.add_argument("--init-db", action="store_true", help="Create tables")
    parser.add_argument("--load-staging", action="store_true", help="Load staging data")
    parser.add_argument("--build-warehouse", action="store_true", help="Build dimensions and facts")
    parser.add_argument("--validate", action="store_true", help="Run validation checks")
    parser.add_argument("--all", action="store_true", help="Run full pipeline")

    args = parser.parse_args()
    conn = get_conn()

    if args.all:
        init_db(conn)
        load_staging_data(conn)
        build_warehouse(conn)
        validate(conn)
        return

    if args.init_db:
        init_db(conn)
    if args.load_staging:
        load_staging_data(conn)
    if args.build_warehouse:
        build_warehouse(conn)
    if args.validate:
        validate(conn)


if __name__ == "__main__":
    main()
