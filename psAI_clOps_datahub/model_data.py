from sqlalchemy import Column, String, Integer
from psAI_clOps_datahub.base import Base


class ModelData(Base):
    __tablename__ = "model_data"

    id = Column(Integer, primary_key=True)
    model_name = Column(String)
    description = Column(String)

    def __init__(self, model_name, description):
        self.model_name = model_name
        self.description = description