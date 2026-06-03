# Execução local (WSL / Ubuntu)

## Pré-requisitos

- Python 3.10+
- Bash (WSL recomendado no Windows)

## Passos

```bash
cd LAKEHOUSE-COM-DATABRICKS-E-ARQUITETURA-MEDALHAO

# 1. Copiar CSVs do material da faculdade
bash scripts/sync_csv_fonte.sh

# 2. Instalar dependências (opcional, só scripts locais)
python3 -m pip install -r requirements.txt

# 3. Criar SQLite e extrair para Landing
python3 scripts/setup_source_db.py
python3 scripts/extract_to_landing.py
```

Saída esperada: 11 arquivos em `data/landing/`.

## Upload para Databricks

No workspace Databricks:

1. **Catalog** → `workspace` → **landing** → **Volumes** → **dados**.
2. **Upload** → selecione todos os `.csv` de `data/landing/`.

Ou use a CLI Databricks / `dbutils.fs.cp` se tiver os arquivos em DBFS temporário.

## MkDocs local

```bash
pip install -r requirements.txt
mkdocs serve
```

Abra [http://127.0.0.1:8000](http://127.0.0.1:8000).

Publicar no GitHub Pages:

```bash
mkdocs gh-deploy --force
```
