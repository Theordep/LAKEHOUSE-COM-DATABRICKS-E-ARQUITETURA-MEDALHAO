# Databricks notebook source
# MAGIC %md
# MAGIC # 000 — Validar arquivos na Landing
# MAGIC
# MAGIC Antes da Job, envie os CSV de `data/landing/` para o volume:
# MAGIC `/Volumes/workspace/landing/dados/`

# COMMAND ----------

caminho = "/Volumes/workspace/landing/dados"
arquivos_esperados = [
    "apolice.csv",
    "carro.csv",
    "cliente.csv",
    "endereco.csv",
    "estado.csv",
    "marca.csv",
    "modelo.csv",
    "municipio.csv",
    "regiao.csv",
    "sinistro.csv",
    "telefone.csv",
]

# COMMAND ----------

listing = [f.name for f in dbutils.fs.ls(caminho)]
faltando = [a for a in arquivos_esperados if a not in listing]
if faltando:
    raise Exception(f"Arquivos ausentes em {caminho}: {faltando}")
print("Landing OK:", len(arquivos_esperados), "arquivos encontrados.")
display(dbutils.fs.ls(caminho))
