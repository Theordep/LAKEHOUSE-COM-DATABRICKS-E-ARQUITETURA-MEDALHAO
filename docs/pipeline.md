# Pipeline e notebooks

## Estrutura do repositório

```
notebooks/
  000_validar_landing.py   # Confere CSVs no Volume
  001_preparar_ambiente.py # Schemas + Volume landing
  002_bronze.py            # Landing → Bronze
  003_silver.py            # Bronze → Silver (DQ)
  004_gold.py              # Silver → Gold (Kimball)
  005_destruir_ambiente.py # Limpeza (opcional)
scripts/
  setup_source_db.py       # CSV → SQLite
  extract_to_landing.py    # SQLite → data/landing/*.csv
data/
  csv_fonte/               # Cópia dos CSVs de referência
  landing/                 # Saída da extração (enviar ao Databricks)
```

## Fluxo local (extração — requisito 1 do PDF)

```bash
bash scripts/sync_csv_fonte.sh
python3 scripts/setup_source_db.py
python3 scripts/extract_to_landing.py
```

Isso simula a extração de **todas** as tabelas de um BD relacional para arquivos CSV na zona Landing.

## Fluxo Databricks

1. Conta [Databricks Free Edition](https://www.databricks.com/learn/free-edition).
2. Importar pasta `notebooks/` (Repos ou upload).
3. Enviar `data/landing/*.csv` para `/Volumes/workspace/landing/dados/`.
4. Executar a Job (ver [job.md](job.md)) ou os notebooks na ordem 000 → 004.

## Silver — Data Quality

A função `renomear_colunas_managed` em `003_silver.py`:

- Renomeia colunas (`cd_` → `codigo_`, `dt_` → `data_`, etc.).
- Remove metadados bronze.
- Adiciona `nome_arquivo_bronze` e `data_arquivo_silver`.

## Gold — modelo dimensional

| Tabela | Tipo | Origem principal |
|--------|------|------------------|
| `dim_carro` | Dimensão | carro + modelo + marca |
| `dim_cliente` | Dimensão | cliente |
| `dim_localidade` | Dimensão | município + estado + região |
| `dim_tempo` | Dimensão | calendário 2023–2026 |
| `fato_sinistro` | Fato | sinistro + dims + apólice |

Cargas dimensionais via `MERGE` (SCD tipo 1). Fato via `INSERT` agregado.
