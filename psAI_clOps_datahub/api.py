from fastapi import FastAPI
from psAI_clOps_datahub.model_data_route import model_data_router

app = FastAPI()
app.include_router(router=model_data_router, tags=["Model Description"])


@app.get("/")
def ping():
    return {"response": "ping to datahub successful"}
