from pathlib import Path
import sqlite3
import yaml


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def load_config() -> dict:
    cfg_path = repo_root() / "etl" / "config" / "config.yaml"
    if not cfg_path.exists():
        cfg_path = repo_root() / "etl" / "config" / "config.example.yaml"
    with cfg_path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def get_conn() -> sqlite3.Connection:
    cfg = load_config()
    db_path = repo_root() / cfg["warehouse"]["path"]
    db_path.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(db_path)


def execute_sql_file(conn: sqlite3.Connection, path: Path) -> None:
    sql_text = path.read_text(encoding="utf-8")
    conn.executescript(sql_text)
    conn.commit()
