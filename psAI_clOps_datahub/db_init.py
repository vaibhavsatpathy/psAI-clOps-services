from psAI_clOps_datahub.base import Session, engine, Base

# 1 - generate database schema
Base.metadata.create_all(engine)