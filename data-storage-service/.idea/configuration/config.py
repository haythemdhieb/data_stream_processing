from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    HOST: str = Field(description="the host of the application", env="HOST", default="localhost")
    PORT: str = Field(description="the port of the application", env="PORT", default="8000")


class MongoSettings(BaseSettings):
    MONGO_PORT: str = Field(description="the mongo database port", env="MONGO_PORT", default="27017")
    MONGO_HOST: str = Field(description="the mongo database host", env="MONGO_HOST", default="localhost")
    MONGO_USER: str = Field(description="mongo user name", env="MONGO_USER", default="root")
    MONGO_PASSWD: str = Field(description="mongo password", env="MONGO_PASSWD", default="pass12345")
    MONGO_COLLECTION: str = Field(description="mongo collection", env="MONGO_COLLECTION", default="data")
    MONGO_DATABASE: str = Field(description="mongo user name", env="MONGO_COLLECTION", default="credit_card")


MongoSettings = MongoSettings()
Settings = Settings()
