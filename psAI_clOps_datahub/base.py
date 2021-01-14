import mlflow

tracking_uri = (
    "http://testuser:password@ec2-18-218-100-222.us-east-2.compute.amazonaws.com"
)
# tracking_uri = "postgresql://postgres:postgres@localhost:5432/"
client = mlflow.tracking.MlflowClient(tracking_uri=tracking_uri)