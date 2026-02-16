from datetime import datetime
from pathlib import Path
import pandas as pd
from etl.utils.logging import get_logger

log = get_logger(__name__)


def extract_incremental_from_csv(csv_path: Path, last_updated_at: str) -> pd.DataFrame:
    """
    Simulated incremental extract from a CRM source.
    In a real system this would query the source DB using a watermark.
    """
    df = pd.read_csv(csv_path)
    if "updated_at" not in df.columns:
        return df

    last_dt = datetime.fromisoformat(last_updated_at)
    df["updated_at"] = pd.to_datetime(df["updated_at"])
    out = df[df["updated_at"] > last_dt]
    log.info("Extracted %s rows from %s", len(out), csv_path.name)
    return out
