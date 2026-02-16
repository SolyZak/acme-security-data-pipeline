CREATE TABLE IF NOT EXISTS stg_visits (
  visit_id     TEXT,
  customer_id  TEXT,
  visit_ts     TEXT,
  channel      TEXT,
  source       TEXT,
  device_type  TEXT,
  city         TEXT,
  ingestion_ts TEXT DEFAULT (datetime('now'))
);
