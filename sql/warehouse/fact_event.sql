CREATE TABLE IF NOT EXISTS fact_event (
  event_key    INTEGER PRIMARY KEY AUTOINCREMENT,
  event_id     TEXT,
  date_key     INTEGER,
  customer_key INTEGER,
  location_key INTEGER,
  device_key   INTEGER,
  event_type   TEXT,
  event_value  REAL,
  visit_id     TEXT,
  event_ts     TEXT,
  load_ts      TEXT DEFAULT (datetime('now')),
  FOREIGN KEY(date_key) REFERENCES dim_date(date_key),
  FOREIGN KEY(customer_key) REFERENCES dim_customer(customer_key),
  FOREIGN KEY(location_key) REFERENCES dim_location(location_key),
  FOREIGN KEY(device_key) REFERENCES dim_device(device_key)
);
