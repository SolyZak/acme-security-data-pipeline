CREATE TABLE IF NOT EXISTS dim_customer (
  customer_key INTEGER PRIMARY KEY AUTOINCREMENT,
  customer_id  TEXT UNIQUE,
  full_name    TEXT,
  email        TEXT,
  phone        TEXT,
  country      TEXT,
  city         TEXT,
  start_date   TEXT,
  end_date     TEXT,
  is_current   INTEGER
);
