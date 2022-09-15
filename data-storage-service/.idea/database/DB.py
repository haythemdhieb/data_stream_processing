import motor.motor_asyncio

from configuration.config import MongoSettings

CONNECTION_STRING = "mongodb://{}:{}@{}:{}".format(MongoSettings.MONGO_USER, MongoSettings.MONGO_PASSWD,
                                                   MongoSettings.MONGO_HOST, int(MongoSettings.MONGO_PORT))

database = motor.motor_asyncio.AsyncIOMotorClient(CONNECTION_STRING)[MongoSettings.MONGO_DATABASE]

credit_card_collection = database[MongoSettings.MONGO_COLLECTION]
