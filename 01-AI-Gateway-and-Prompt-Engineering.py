# Databricks notebook source
# MAGIC %md
# MAGIC ### Set up AI Gateway
# MAGIC
# MAGIC Databricks AI Gateway serves as a consistent front-end that allows you to try out multiple LLMs, manage credentials and constrain their use in production

# COMMAND ----------

# MAGIC %md
# MAGIC #### Step 1 - Install

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


