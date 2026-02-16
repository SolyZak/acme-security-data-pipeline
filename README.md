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

## Data Dictionary
See `docs/data_dictionary.md` for field definitions across staging and warehouse tables.

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

## Makefile Shortcuts
`make init`, `make load`, `make build`, `make validate`, `make run`, `make clean`

## Example Queries
Event counts by type:
```sql
SELECT event_type, COUNT(*) AS cnt
FROM fact_event
GROUP BY event_type
ORDER BY cnt DESC;
```

Expected result:
| event_type | cnt |
| --- | --- |
| view | 3 |
| click | 2 |
| conversion | 2 |

Conversion value by country:
```sql
SELECT l.country, COUNT(*) AS conversions, ROUND(SUM(f.event_value), 2) AS total_value
FROM fact_event f
JOIN dim_location l ON f.location_key = l.location_key
WHERE f.event_type = 'conversion'
GROUP BY l.country
ORDER BY total_value DESC;
```

Expected result:
| country | conversions | total_value |
| --- | --- | --- |
| Bahrain | 1 | 149.00 |
| Kuwait | 1 | 99.99 |

## Roadmap
- Add lightweight orchestration (cron or task runner)
- Add test suite for validation logic
- Add incremental load state tracking table

## Safety Note
Everything in this repository is fictional and synthetic. No real company names, schemas, data, or business logic are included.

## License
MIT
