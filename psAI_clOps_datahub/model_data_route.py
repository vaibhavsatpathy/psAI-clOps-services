from fastapi import APIRouter
from psAI_clOps_datahub.model_data_crud import (
    get_all_models,
    get_model_desc,
)

model_data_router = APIRouter()


@model_data_router.get("/get_all_models")
async def get_all_model_desc_api(no_of_models: int = 10):
    models = get_all_models(num_of_models=no_of_models)
    return {"Models": models}


@model_data_router.get("/get_model_data/")
async def get_model_desc_api(model_name: str = "Default"):
    model_data = get_model_desc(experiment_name=model_name)
    return {"Model data": model_data}
