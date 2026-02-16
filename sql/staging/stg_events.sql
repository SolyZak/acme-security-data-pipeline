CREATE TABLE IF NOT EXISTS stg_events (
  event_id     TEXT,
  visit_id     TEXT,
  customer_id  TEXT,
  event_ts     TEXT,
  event_type   TEXT,
  event_value  REAL,
  ingestion_ts TEXT DEFAULT (datetime('now'))
);
