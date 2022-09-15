import re
from typing import List

import requests
from loguru import logger

from configurations.configurations import DATA_STORAGE_URL, CLASSIFICATION_URL


def send_article_classification(article: dict) -> str:
    """
    This function sends the text in the article to the classification service and
    returns the class of the article
    :param article: the text of the article
    :return: the class of the article
    """
    try:
        response = requests.post(CLASSIFICATION_URL, json=article)
        saga = response.json().get("label")
        return saga
    except requests.ConnectionError:
        logger.error("Invalid url {}".format(CLASSIFICATION_URL))


def send_results_data_storage_service(result: dict) -> bool:
    """
    This function sends the result (article's saga and the mentioned entities) to the data storage service
    :param result: result of the processing containing two fields: extracted entities and the corresponding saga class
    :return: the status of storage
    """
    try:
        response = requests.post(DATA_STORAGE_URL + "?saga={}".format(result.get("saga")), json=result)
        if response:
            return True
        else:
            return False
    except requests.ConnectionError:
        logger.error("Invalid url {}".format(DATA_STORAGE_URL))


def extract_entities(entities_path: str, article: dict) -> List[str]:
    """
    :param entities_path: path of a txt file containing all the entities in the three sagas
    :param article: dict containing text and id of the article
    :return: list of entities/characters found in the article
    """
    found_characters = []
    with open(entities_path, "r") as file:
        entities = file.readlines()
    entities = " ".join(entities).split(" ")
    for character in entities:
        if re.sub(r'[^a-zA-Z]', "", character.lower()) in article.get("text"):
            found_characters.append(re.sub(r'[^a-zA-Z]', "", character.lower()))
    return found_characters
