# Databricks notebook source
# MAGIC %md
# MAGIC # 003 — Silver: Data Quality (Bronze → Silver)

# COMMAND ----------

from pyspark.sql import functions as F


def _apply_name_rules(colname: str) -> str:
    n = colname.upper()
    n = n.replace("CD_", "CODIGO_")
    n = n.replace("VL_", "VALOR_")
    n = n.replace("DT_", "DATA_")
    n = n.replace("NM_", "NOME_")
    n = n.replace("DS_", "DESCRICAO_")
    n = n.replace("NR_", "NUMERO_")
    n = n.replace("_UF", "_UNIDADE_FEDERATIVA")
    return n


def _safe_drop(df, cols):
    existing = set(df.columns)
    to_drop = [c for c in cols if c in existing]
    return df.drop(*to_drop) if to_drop else df


def renomear_colunas_managed(src_fqn: str, dest_fqn: str = None):
    dest_fqn = dest_fqn or src_fqn
    df = spark.read.format("delta").table(src_fqn)
    new_cols = [_apply_name_rules(c) for c in df.columns]
    df = df.toDF(*new_cols)
    df = _safe_drop(df, ["DATA_HORA_BRONZE", "NOME_ARQUIVO"])
    df = (
        df.withColumn("NOME_ARQUIVO_BRONZE", F.lit(src_fqn))
        .withColumn("DATA_ARQUIVO_SILVER", F.current_timestamp())
    )
    df.write.format("delta").mode("overwrite").saveAsTable(dest_fqn)
    return dest_fqn

# COMMAND ----------

tabelas = [
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

for t in tabelas:
    renomear_colunas_managed(f"bronze.{t}", f"silver.{t}")
    print(f"OK silver.{t}")

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW TABLES IN silver

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE EXTENDED silver.apolice
