# Trabalho 3 — Lakehouse com Databricks e Arquitetura Medalhão

Projeto acadêmico da disciplina de **Arquitetura de Dados** (SATC): pipeline **Landing → Bronze → Silver → Gold** no **Databricks Free Edition**, com orquestração por **Job** e documentação em MkDocs.

## Objetivo

Construir um pipeline de dados implementando a arquitetura **Medalhão** (multi-hop), conforme o enunciado do Trabalho 3:

1. Extrair todas as tabelas de um banco **relacional** (SQLite) para a zona **Landing** em CSV.
2. Gravar **Bronze** em Delta Lake a partir dos CSVs.
3. Aplicar **Data Quality** na camada **Silver**.
4. Publicar modelo **dimensional Kimball** na camada **Gold**.
5. Encadear notebooks em uma **Job** Databricks sequencial.

## Repositório

[Código no GitHub](https://github.com/Theordep/LAKEHOUSE-COM-DATABRICKS-E-ARQUITETURA-MEDALHAO)

## Equipe

Pedro Ernesto · Carlos Eduardo · Axel Filastro

## Evolução dos trabalhos

| Trabalho | Foco |
|----------|------|
| [Trabalho 1](https://github.com/Theordep/trabalho-arquitetura-de-dados) | PySpark local — Delta Lake e Iceberg |
| [Trabalho 2](https://github.com/Theordep/trabalho-spark-delta-minio) | Spark + MinIO — Landing e Bronze |
| **Trabalho 3** (este) | Databricks — Medalhão completo até Gold |
