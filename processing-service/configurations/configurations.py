import os

DATA_STORAGE_URL = os.environ.get("STORAGE_URL", "localhost:8000/articles/")
CLASSIFICATION_URL = os.environ.get("CLASSIFICATION_URL", "localhost:4000/predict")
ENTITIES = os.environ.get("ENTITIES_PATH", "entities.txt")
