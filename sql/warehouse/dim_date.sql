CREATE TABLE IF NOT EXISTS dim_date (
  date_key     INTEGER PRIMARY KEY,
  full_date    TEXT,
  year         INTEGER,
  month        INTEGER,
  day          INTEGER,
  week_of_year INTEGER
);
