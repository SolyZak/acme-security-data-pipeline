# ETL Overview

This folder contains a simplified, portfolio-ready ETL layout:
- `extract/`: simulated incremental extraction
- `transform/`: staging loader and warehouse builder
- `load/`: placeholder for separate load step
- `validation/`: data quality checks
- `run_pipeline.py`: command-line runner

The pipeline reads synthetic CSV files and writes to a local SQLite database.
