import uvicorn
from fastapi import FastAPI

from configuration.config import Settings
from routers import articles

app = FastAPI()

app.include_router(articles.router, tags=["articles"], prefix="/articles")


@app.get("/", tags=["Home"])
async def read_root():
    return {"message": "Mongo DB storage microservice"}


if __name__ == '__main__':
    uvicorn.run(app, host=Settings.HOST, port=int(Settings.PORT))
