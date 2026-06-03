"""Extrai todas as tabelas do SQLite para CSV na zona Landing (requisito Trabalho 3)."""
from pathlib import Path
import sqlite3

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "data" / "source.db"
LANDING_DIR = ROOT / "data" / "landing"


def extract_all_tables():
    if not DB_PATH.exists():
        raise FileNotFoundError(
            f"Banco não encontrado: {DB_PATH}. Execute: python scripts/setup_source_db.py"
        )
    LANDING_DIR.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name"
        )
        tables = [row[0] for row in cursor.fetchall()]
        for table in tables:
            df = pd.read_sql_query(f"SELECT * FROM {table}", conn)
            out = LANDING_DIR / f"{table}.csv"
            df.to_csv(out, index=False)
            print(f"Landing: {out} ({len(df)} linhas)")
    print(f"\n{len(tables)} arquivos CSV em {LANDING_DIR}")
    print("Envie-os para: /Volumes/workspace/landing/dados/ no Databricks")


if __name__ == "__main__":
    extract_all_tables()
