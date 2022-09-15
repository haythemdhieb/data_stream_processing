import uvicorn
from fastapi import FastAPI

from configuration.config import Settings
from routers import credit_card_routes

app = FastAPI()

app.include_router(credit_card_routes.router, tags=["credit_card"], prefix="/credit_card")


@app.get("/", tags=["Home"])
async def read_root():
    return {"message": "Mongo DB storage microservice"}


if __name__ == '__main__':
    uvicorn.run(app, host=Settings.HOST, port=int(Settings.PORT))
