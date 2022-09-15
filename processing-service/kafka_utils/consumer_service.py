import re
import time

from confluent_kafka import Consumer
from loguru import logger

from configurations.configurations import ENTITIES
from configurations.kafka_setup import KAFKA_SERVERS, KAFKA_ID, OFFSET, TOPIC
from helpers.utils import extract_entities, send_article_classification, send_results_data_storage_service


def consumer_init():
    consumer = Consumer({
        'bootstrap.servers': KAFKA_SERVERS,
        'group.id': KAFKA_ID,
        'auto.offset.reset': OFFSET
    })
    consumer.subscribe([TOPIC])
    return consumer


def consumer_loop() -> None:
    """
    This functions consumes a message (Kafka consumer) from a given topic
               and sends the message to processing if it exists
    """
    consumer = consumer_init()
    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            logger.info("No message received")
        else:
            logger.info('Received message: {}'.format(msg.value().decode('utf-8')))
            article = msg.value().decode('utf-8')
            article = re.sub(r'[^a-zA-Z ]', "", article.lower())
            article_data = {"text": article}
            article_saga = send_article_classification(article_data)
            entities_found = extract_entities(ENTITIES, article_data)
            logger.info(entities_found)
            result = {"saga": article_saga, "text": article, "entities": entities_found, "time": int(time.time())}
            send_results_data_storage_service(result)
