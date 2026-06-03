# Databricks notebook source
# MAGIC %md
# MAGIC # 005 - Atifidade Pratica - Lakehouse - Destruindo ambiente

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Apagar todas as tabelas da camada bronze
# MAGIC DROP SCHEMA IF EXISTS workspace.bronze CASCADE;
# MAGIC 
# MAGIC -- Apagar todas as tabelas da camada silver
# MAGIC DROP SCHEMA IF EXISTS workspace.silver CASCADE;
# MAGIC 
# MAGIC -- Apagar todas as tabelas da camada gold
# MAGIC DROP SCHEMA IF EXISTS workspace.gold CASCADE;
# MAGIC 
# MAGIC -- Apagar todas as tabelas e volumes da camada landing
# MAGIC DROP SCHEMA IF EXISTS workspace.landing CASCADE;

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW SCHEMAS IN workspace;

# COMMAND ----------
