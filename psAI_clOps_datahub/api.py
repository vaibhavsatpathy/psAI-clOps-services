from fastapi import FastAPI
from psAI_clOps_datahub.model_data_route import model_data_router
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(router=model_data_router, tags=["Model Description"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def ping():
    return {"response": "ping to datahub successful"}
