from sqlalchemy import create_engine, MetaData, event, DDL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:postgres@localhost:5432/")
Session = sessionmaker(bind=engine)
metadata = MetaData(schema="mlops_schema")

Base = declarative_base(metadata=metadata)
Base.metadata.create_all(engine)
event.listen(
    Base.metadata,
    "before_create",
    DDL("CREATE SCHEMA IF NOT EXISTS mlops_schema"),
)
