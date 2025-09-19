import dagshub
dagshub.init(repo_owner='ahmed-el-shenawy', repo_name='dagshub-session', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)
