"""Cria banco SQLite relacional a partir dos CSVs de seguros (simula sistema de origem)."""
from pathlib import Path
import sqlite3

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
CSV_DIR = ROOT / "data" / "csv_fonte"
DB_PATH = ROOT / "data" / "source.db"

TABLES = [
    "apolice",
    "carro",
    "cliente",
    "endereco",
    "estado",
    "marca",
    "modelo",
    "municipio",
    "regiao",
    "sinistro",
    "telefone",
]


def create_database():
    if not CSV_DIR.exists():
        raise FileNotFoundError(f"Pasta de CSVs não encontrada: {CSV_DIR}")
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(DB_PATH) as conn:
        for table in TABLES:
            csv_path = CSV_DIR / f"{table}.csv"
            if not csv_path.exists():
                raise FileNotFoundError(csv_path)
            df = pd.read_csv(csv_path)
            df.to_sql(table, conn, index=False, if_exists="replace")
            print(f"Tabela '{table}': {len(df)} linhas")
    print(f"SQLite criado em: {DB_PATH}")


if __name__ == "__main__":
    create_database()
