# Databricks notebook source
# MAGIC %md
# MAGIC # 001 - Atifidade Pratica - Lakehouse - Preparando ambiente

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE SCHEMA IF NOT EXISTS workspace.landing
# MAGIC COMMENT 'Schema/Database para dados bronze (delta)';
# MAGIC 
# MAGIC CREATE VOLUME IF NOT EXISTS workspace.landing.dados
# MAGIC COMMENT 'Volume para dados brutos criados no schema/database landing';
# MAGIC 
# MAGIC CREATE SCHEMA IF NOT EXISTS workspace.bronze
# MAGIC COMMENT 'Schema/Database para dados bronze (delta)';
# MAGIC 
# MAGIC CREATE SCHEMA IF NOT EXISTS workspace.silver
# MAGIC COMMENT 'Schema/Database para dados silver (delta)';
# MAGIC 
# MAGIC CREATE SCHEMA IF NOT EXISTS workspace.gold
# MAGIC COMMENT 'Schema/Database para dados gold (delta) - modelagem dimensional';

# COMMAND ----------
