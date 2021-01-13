from sqlalchemy import create_engine, MetaData, event, DDL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import mlflow

tracking_uri = (
    "http://testuser:password@ec2-18-218-100-222.us-east-2.compute.amazonaws.com"
)
# tracking_uri = "postgresql://postgres:postgres@localhost:5432/"
client = mlflow.tracking.MlflowClient(tracking_uri=tracking_uri)
engine = create_engine("postgresql://postgres:postgres@localhost:5432/")
Session = sessionmaker(bind=engine)
metadata = MetaData(schema="mlops_schema")

Base = declarative_base(metadata=metadata)
event.listen(
    Base.metadata,
    "before_create",
    DDL("CREATE SCHEMA IF NOT EXISTS mlops_schema"),
)
