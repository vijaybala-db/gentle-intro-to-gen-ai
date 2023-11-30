# Databricks notebook source
# MAGIC %md
# MAGIC # A Gentle, Hands On Introduction to Gen AI
# MAGIC
# MAGIC The following content is designed to get a partner started on their Gen AI journey on the Databricks and MosaicML platform. It consists of a simple tutorial that partners can run in any compatible environment to get hands on experience with basic Gen AI features.
# MAGIC
# MAGIC It contains the following modules:
# MAGIC
# MAGIC 1. AI Gateway and Prompt Engineering UI
# MAGIC
# MAGIC 2. Retrieval Augmented Generation (RAG)
# MAGIC
# MAGIC 3. Fine tuning to create a custom model
# MAGIC
# MAGIC The demo assets are designed to be easily deployable to any Databricks workspace.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Prerequisites
# MAGIC
# MAGIC 1. Databricks workspace with Serverless enabled
# MAGIC
# MAGIC 2. API key for OpenAI
# MAGIC
# MAGIC 3. MosaicML account and API key - See below for how to get it
# MAGIC
# MAGIC ##### How to get a MosaicML account and API key
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ## Module 1 - AI Gateway and Prompt Engineering UI

# COMMAND ----------

# MAGIC %md
# MAGIC ### Set up AI Gateway
# MAGIC
# MAGIC Databricks AI Gateway serves as a consistent front-end that allows you to try out multiple LLMs, manage credentials and constrain their use in production

# COMMAND ----------

# MAGIC %md
# MAGIC #### Step 1 - Set up Databricks Secrets with API keys

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC #### Step 2 - Install

# COMMAND ----------

# MAGIC %pip install mlflow[gateway]

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Step 2 - Set the Gateway URI

# COMMAND ----------

from mlflow.gateway import set_gateway_uri
set_gateway_uri(gateway_uri='databricks')

# COMMAND ----------

# MAGIC %md
# MAGIC #### Step 3 - Set up Databricks Secrets with API keys to OpenAI, MosaicML, etc.
# MAGIC
# MAGIC Note: before you run the following code, please use the Databricks CLI to create a secret scope and secret keys for each LLM API you wish to access. For example, your CLI commands might be as follows:
# MAGIC
# MAGIC ```
# MAGIC # Install the Databricks CLI
# MAGIC curl -fsSL https://raw.githubusercontent.com/databricks/setup-cli/main/install.sh | sh
# MAGIC ```

# COMMAND ----------

dbutils.secrets.help()

# COMMAND ----------


