# Data Dictionary

All fields are synthetic and safe for public use.

## Staging Tables

### stg_customers
| Column | Type | Description |
| --- | --- | --- |
| customer_id | text | Synthetic customer identifier |
| full_name | text | Synthetic full name |
| email | text | Synthetic email |
| phone | text | Synthetic phone |
| country | text | Country name |
| city | text | City name |
| created_at | text | Customer creation timestamp |
| updated_at | text | Customer update timestamp |
| ingestion_ts | text | Load timestamp |

### stg_visits
| Column | Type | Description |
| --- | --- | --- |
| visit_id | text | Synthetic visit identifier |
| customer_id | text | Synthetic customer identifier |
| visit_ts | text | Visit timestamp |
| channel | text | Acquisition channel |
| source | text | Traffic source |
| device_type | text | Device type |
| city | text | City name |
| ingestion_ts | text | Load timestamp |

### stg_events
| Column | Type | Description |
| --- | --- | --- |
| event_id | text | Synthetic event identifier |
| visit_id | text | Synthetic visit identifier |
| customer_id | text | Synthetic customer identifier |
| event_ts | text | Event timestamp |
| event_type | text | Event type |
| event_value | real | Event value |
| ingestion_ts | text | Load timestamp |

## Warehouse Tables

### dim_customer
| Column | Type | Description |
| --- | --- | --- |
| customer_key | integer | Surrogate key |
| customer_id | text | Natural key |
| full_name | text | Synthetic full name |
| email | text | Synthetic email |
| phone | text | Synthetic phone |
| country | text | Country name |
| city | text | City name |
| start_date | text | SCD start date |
| end_date | text | SCD end date |
| is_current | integer | Current record flag |

### dim_date
| Column | Type | Description |
| --- | --- | --- |
| date_key | integer | YYYYMMDD key |
| full_date | text | Full date |
| year | integer | Year |
| month | integer | Month |
| day | integer | Day |
| week_of_year | integer | ISO week number |

### dim_location
| Column | Type | Description |
| --- | --- | --- |
| location_key | integer | Surrogate key |
| country | text | Country name |
| city | text | City name |

### dim_device
| Column | Type | Description |
| --- | --- | --- |
| device_key | integer | Surrogate key |
| device_type | text | Device type |

### fact_event
| Column | Type | Description |
| --- | --- | --- |
| event_key | integer | Surrogate key |
| event_id | text | Event identifier |
| date_key | integer | Date key |
| customer_key | integer | Customer surrogate key |
| location_key | integer | Location surrogate key |
| device_key | integer | Device surrogate key |
| event_type | text | Event type |
| event_value | real | Event value |
| visit_id | text | Visit identifier |
| event_ts | text | Event timestamp |
| load_ts | text | Load timestamp |
