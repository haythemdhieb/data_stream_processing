import os


KAFKA_SERVERS = os.environ.get("KAFKA_SERVERS", "kafka")
KAFKA_ID = os.environ.get("KAFKA_ID", "mygroup")
OFFSET = os.environ.get("KAFKA_RESET", "earliest")
TOPIC = os.environ.get("KAFKA_TOPIC", "events")

