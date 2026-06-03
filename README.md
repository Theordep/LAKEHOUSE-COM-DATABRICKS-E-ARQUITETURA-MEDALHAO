# Lakehouse com Databricks — Arquitetura Medalhão (Trabalho 3)

[![Documentação](https://img.shields.io/badge/docs-MkDocs-blue)](docs/index.md)
[![Databricks](https://img.shields.io/badge/Databricks-Free%20Edition-red)](https://www.databricks.com/learn/free-edition)

Pipeline **Landing → Bronze → Silver → Gold** no **Databricks Free Edition**, domínio de **seguros automotivos**, com extração relacional (SQLite → CSV), Data Quality na Silver, modelo **Kimball** na Gold e orquestração por **Job**.

**Repositório:** [github.com/Theordep/LAKEHOUSE-COM-DATABRICKS-E-ARQUITETURA-MEDALHAO](https://github.com/Theordep/LAKEHOUSE-COM-DATABRICKS-E-ARQUITETURA-MEDALHAO)

**Equipe:** Pedro Ernesto · Carlos Eduardo · Axel Filastro

---

## Conformidade com o enunciado (PDF)

| Requisito | Implementação |
|-----------|----------------|
| Extração de todas as tabelas → Landing (CSV) | `scripts/setup_source_db.py` + `scripts/extract_to_landing.py` |
| Bronze: CSV → Delta | `notebooks/002_bronze.py` |
| Silver: Data Quality | `notebooks/003_silver.py` |
| Gold: dimensões Kimball | `notebooks/004_gold.py` |
| Job sequencial | `jobs/medalhao_pipeline.job.yml` + [docs/job.md](docs/job.md) |
| Repositório próprio + README + MkDocs | Este repositório |

---

## Estrutura

```
├── README.md
├── mkdocs.yml
├── requirements.txt
├── docs/                 # MkDocs
├── notebooks/            # Notebooks Databricks (000–005)
├── scripts/              # Extração local SQLite → Landing
├── data/
│   ├── csv_fonte/        # CSVs de referência
│   └── landing/          # Saída da extração (upload no Volume)
├── jobs/                 # Definição da Job
└── DOCS-FACUL/           # Material da aula (referência)
```

---

## Início rápido

### 1. Extração local (WSL / Ubuntu)

```bash
cd LAKEHOUSE-COM-DATABRICKS-E-ARQUITETURA-MEDALHAO
bash scripts/sync_csv_fonte.sh
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python scripts/setup_source_db.py
.venv/bin/python scripts/extract_to_landing.py
```

### 2. Databricks

1. Crie conta na [Databricks Free Edition](https://www.databricks.com/learn/free-edition).
2. Importe a pasta `notebooks/` no workspace (Git folder ou upload).
3. Faça upload dos arquivos de `data/landing/` para `/Volumes/workspace/landing/dados/`.
4. Crie a Job conforme [docs/job.md](docs/job.md) (ordem: 000 → 001 → 002 → 003 → 004).

### 3. Documentação

```bash
pip install -r requirements.txt
mkdocs serve
# Publicar: mkdocs gh-deploy --force
```

---

## Notebooks

| Arquivo | Camada |
|---------|--------|
| `000_validar_landing.py` | Validação Landing |
| `001_preparar_ambiente.py` | Schemas + Volume |
| `002_bronze.py` | Bronze |
| `003_silver.py` | Silver |
| `004_gold.py` | Gold |
| `005_destruir_ambiente.py` | Limpeza (manual) |

---

## Trabalhos anteriores

- [Trabalho 1 — Delta + Iceberg (local)](https://github.com/Theordep/trabalho-arquitetura-de-dados)
- [Trabalho 2 — Spark + MinIO (Landing/Bronze)](https://github.com/Theordep/trabalho-spark-delta-minio)

---

## Referências

- [Medallion Architecture — Databricks](https://www.databricks.com/br/glossary/medallion-architecture)
- Material em `DOCS-FACUL/` (notebooks `.dbc` e CSVs da disciplina)
