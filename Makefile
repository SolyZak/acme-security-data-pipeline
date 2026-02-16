.PHONY: init load build validate run clean

init:
	python -m etl.run_pipeline --init-db

load:
	python -m etl.run_pipeline --load-staging

build:
	python -m etl.run_pipeline --build-warehouse

validate:
	python -m etl.run_pipeline --validate

run:
	python -m etl.run_pipeline --all

clean:
	rm -f data/warehouse.db
