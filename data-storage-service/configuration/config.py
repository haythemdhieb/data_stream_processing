from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    HOST: str = Field(description="the host of the application", env="HOST", default="0.0.0.0")
    PORT: str = Field(description="the port of the application", env="PORT", default="8550")


class MongoSettings(BaseSettings):
    MONGO_PORT: str = Field(description="the mongo database port", env="MONGO_PORT", default="27017")
    MONGO_HOST: str = Field(description="the mongo database host", env="MONGO_HOST", default="mongodb")
    MONGO_USER: str = Field(description="mongo user name", env="MONGO_USER", default="root")
    MONGO_PASSWD: str = Field(description="mongo password", env="MONGO_PASSWD", default="pass12345")
    MONGO_COLLECTION_GOT: str = Field(description="mongo collection for GOT saga", env="MONGO_COLLECTION_GOT", default="got")
    MONGO_COLLECTION_LOTR: str = Field(description="mongo collection for LOTR saga", env="MONGO_COLLECTION_LOTR", default="lotr")
    MONGO_COLLECTION_HP: str = Field(description="mongo collection for HP saga", env="MONGO_COLLECTION_HP", default="hp")
    MONGO_DATABASE: str = Field(description="mongo database name", env="MONGO_DATABASE", default="saga")


MongoSettings = MongoSettings()
Settings = Settings()
