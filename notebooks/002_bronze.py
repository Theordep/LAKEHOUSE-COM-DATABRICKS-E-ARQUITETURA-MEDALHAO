# Databricks notebook source
# MAGIC %md
# MAGIC # 002 — Bronze: CSV (Landing) → Delta Lake

# COMMAND ----------

caminho_landing = "/Volumes/workspace/landing/dados"

# COMMAND ----------

display(dbutils.fs.ls(caminho_landing))

# COMMAND ----------

df_apolice = spark.read.option("inferSchema", "true").option("header", "true").csv(f"{caminho_landing}/apolice.csv")
df_carro = spark.read.option("inferSchema", "true").option("header", "true").csv(f"{caminho_landing}/carro.csv")
df_cliente = spark.read.option("inferSchema", "true").option("header", "true").csv(f"{caminho_landing}/cliente.csv")
df_endereco = spark.read.option("inferSchema", "true").option("header", "true").csv(f"{caminho_landing}/endereco.csv")
df_estado = spark.read.option("inferSchema", "true").option("header", "true").csv(f"{caminho_landing}/estado.csv")
df_marca = spark.read.option("inferSchema", "true").option("header", "true").csv(f"{caminho_landing}/marca.csv")
df_modelo = spark.read.option("inferSchema", "true").option("header", "true").csv(f"{caminho_landing}/modelo.csv")
df_municipio = spark.read.option("inferSchema", "true").option("header", "true").csv(f"{caminho_landing}/municipio.csv")
df_regiao = spark.read.option("inferSchema", "true").option("header", "true").csv(f"{caminho_landing}/regiao.csv")
df_sinistro = spark.read.option("inferSchema", "true").option("header", "true").csv(f"{caminho_landing}/sinistro.csv")
df_telefone = spark.read.option("inferSchema", "true").option("header", "true").csv(f"{caminho_landing}/telefone.csv")

# COMMAND ----------

from pyspark.sql.functions import current_timestamp, lit

df_apolice = df_apolice.withColumn("data_hora_bronze", current_timestamp()).withColumn("nome_arquivo", lit("apolice.csv"))
df_carro = df_carro.withColumn("data_hora_bronze", current_timestamp()).withColumn("nome_arquivo", lit("carro.csv"))
df_cliente = df_cliente.withColumn("data_hora_bronze", current_timestamp()).withColumn("nome_arquivo", lit("cliente.csv"))
df_endereco = df_endereco.withColumn("data_hora_bronze", current_timestamp()).withColumn("nome_arquivo", lit("endereco.csv"))
df_estado = df_estado.withColumn("data_hora_bronze", current_timestamp()).withColumn("nome_arquivo", lit("estado.csv"))
df_marca = df_marca.withColumn("data_hora_bronze", current_timestamp()).withColumn("nome_arquivo", lit("marca.csv"))
df_modelo = df_modelo.withColumn("data_hora_bronze", current_timestamp()).withColumn("nome_arquivo", lit("modelo.csv"))
df_municipio = df_municipio.withColumn("data_hora_bronze", current_timestamp()).withColumn("nome_arquivo", lit("municipio.csv"))
df_regiao = df_regiao.withColumn("data_hora_bronze", current_timestamp()).withColumn("nome_arquivo", lit("regiao.csv"))
df_sinistro = df_sinistro.withColumn("data_hora_bronze", current_timestamp()).withColumn("nome_arquivo", lit("sinistro.csv"))
df_telefone = df_telefone.withColumn("data_hora_bronze", current_timestamp()).withColumn("nome_arquivo", lit("telefone.csv"))

# COMMAND ----------

df_apolice.write.format("delta").mode("overwrite").saveAsTable("bronze.apolice")
df_carro.write.format("delta").mode("overwrite").saveAsTable("bronze.carro")
df_cliente.write.format("delta").mode("overwrite").saveAsTable("bronze.cliente")
df_endereco.write.format("delta").mode("overwrite").saveAsTable("bronze.endereco")
df_estado.write.format("delta").mode("overwrite").saveAsTable("bronze.estado")
df_marca.write.format("delta").mode("overwrite").saveAsTable("bronze.marca")
df_modelo.write.format("delta").mode("overwrite").saveAsTable("bronze.modelo")
df_municipio.write.format("delta").mode("overwrite").saveAsTable("bronze.municipio")
df_regiao.write.format("delta").mode("overwrite").saveAsTable("bronze.regiao")
df_sinistro.write.format("delta").mode("overwrite").saveAsTable("bronze.sinistro")
df_telefone.write.format("delta").mode("overwrite").saveAsTable("bronze.telefone")

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW TABLES IN bronze

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE DETAIL bronze.apolice
