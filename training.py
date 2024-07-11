import mlflow

mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("android_malware_detection")

with mlflow.start_run():
    mlflow.log_param("param_name", param_value)
    mlflow.log_metric("metric_name", metric_value)
    mlflow.log_artifact("path/to/artifact")
