from configuration.config import MongoSettings
from pymongo import MongoClient

CONNECTION_STRING = "mongodb://{}:{}@{}:{}".format(MongoSettings.MONGO_USER, MongoSettings.MONGO_PASSWD,
                                                      MongoSettings.MONGO_HOST, int(MongoSettings.MONGO_PORT))

client = MongoClient(CONNECTION_STRING)
database = client[MongoSettings.MONGO_DATABASE]
hp_collection = database[MongoSettings.MONGO_COLLECTION_HP]
lotr_collection = database[MongoSettings.MONGO_COLLECTION_LOTR]
got_collection = database[MongoSettings.MONGO_COLLECTION_GOT]
saga_collections = {"hp": hp_collection, "lotr": lotr_collection, "got": got_collection}
