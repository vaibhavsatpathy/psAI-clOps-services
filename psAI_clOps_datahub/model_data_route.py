from fastapi import APIRouter
from psAI_clOps_datahub.model_data_crud import (
    model_data_crud,
    get_all_models,
    get_model_desc,
    delete_model_desc,
)

model_data_router = APIRouter()


@model_data_router.post("/add_model_description")
async def model_data_func_api():
    model_data_crud()
    return {"Sucess": "YO"}


@model_data_router.get("/get_all_model_description")
async def get_all_model_desc_api():
    models = get_all_models()
    return {"Sucess": models}


@model_data_router.get("/get_model_description")
async def get_model_desc_api():
    model_data = get_model_desc()
    return {"Sucess": model_data}


@model_data_router.post("/delete_model")
async def delete_model_desc_api():
    return {"Sucess": "YO"}
