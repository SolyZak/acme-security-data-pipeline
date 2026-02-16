# Architecture

This project shows a generic, safe data pipeline for a fictional company operating at large scale in the Gulf and Middle East region.

Flow:
1. CRM source system (generic relational DB)
2. Incremental extract by `updated_at`
3. Staging tables for raw landing data
4. Warehouse star schema (dimensions + facts)
5. Data validation gates
6. BI dashboards and reporting

All data, schemas, and logic are synthetic.
