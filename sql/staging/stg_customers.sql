CREATE TABLE IF NOT EXISTS stg_customers (
  customer_id  TEXT,
  full_name    TEXT,
  email        TEXT,
  phone        TEXT,
  country      TEXT,
  city         TEXT,
  created_at   TEXT,
  updated_at   TEXT,
  ingestion_ts TEXT DEFAULT (datetime('now'))
);
