import uvicorn
from psAI_clOps_datahub.api import app

# import psAI_clOps_datahub.db_init


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
