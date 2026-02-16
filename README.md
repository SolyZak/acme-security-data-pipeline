# Acme Security Regional Data Pipeline (Portfolio)

![CI](https://github.com/solyzak/acme-security-data-pipeline/actions/workflows/ci.yml/badge.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## Problem Statement
Acme Security is a fictional company operating at large scale across the Gulf and Middle East region. The business needs reliable analytics for customer engagement and operational reporting. This project demonstrates a safe, generic data pipeline that extracts from a CRM source, lands data in staging, transforms to a star schema, and supports dashboards. All data and logic are synthetic and safe for public use.

## Architecture
- Source: Operational CRM (generic relational DB)
- Extract: Incremental extraction by `updated_at` watermark
- Staging: Raw landing tables (`stg_customers`, `stg_visits`, `stg_events`)
- Transform: Star schema with dimensions and facts
- Validation: Basic data quality checks (row counts, null keys)
- Output: Analytics-ready warehouse tables for BI dashboards

See `docs/diagram.txt` and `docs/architecture.md` for the diagram description.

## Technologies Used
- Python 3 (ETL + validation)
- SQL (schema + transforms)
- SQLite (local demo warehouse)
- Pandas (optional)

## Scalability Considerations
- Incremental loading with watermarks
- Staging layer to isolate raw data
- Star schema optimized for reporting
- Data validation gates
- In production, this pattern scales to high-volume regional data using distributed storage and orchestration

## How to Run Locally
1. Create and activate a virtual environment.
2. Install dependencies: `pip install -r requirements.txt`
3. Initialize the local SQLite warehouse: `python -m etl.run_pipeline --init-db`
4. Load synthetic data into staging: `python -m etl.run_pipeline --load-staging`
5. Build warehouse tables: `python -m etl.run_pipeline --build-warehouse`
6. Run validation checks: `python -m etl.run_pipeline --validate`

## Safety Note
Everything in this repository is fictional and synthetic. No real company names, schemas, data, or business logic are included.

## What to Verify Before Publishing to GitHub
1. No real company names, client names, or internal project references
2. No real database schemas, table names, or column names
3. All sample data is synthetic and non-identifiable
4. No API keys, passwords, or connection strings
5. No internal hostnames, URLs, or file paths
6. No proprietary business logic or calculations that mirror real systems
7. No sensitive data in git history, notebooks, or logs
8. README and docs contain only generic, safe descriptions

## License
MIT
