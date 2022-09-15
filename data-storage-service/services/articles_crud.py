from collections import Counter
from typing import List

from bson.objectid import ObjectId

from database.DB import saga_collections
from utils.helpers import article_helper


def get_all_articles(saga: str) -> List:
    """
    :param saga: one of the three sagas
    :return: list of  all the articles data
    """
    articles = []
    results = saga_collections.get(saga).find({})
    for result in results:
        result['_id'] = str(result['_id'])
        articles.append(result)
    return articles


def add_article_data(saga: str, article: dict) -> dict:
    """
    :param saga: one of the three sagas
    :param article: all the information related to the article that will be inserted to the database
    :return: inserted article info
    """
    article = saga_collections.get(saga).insert_one(article)
    inserted_article =  saga_collections.get(saga).find_one({"_id": article.inserted_id})
    print(article_helper(inserted_article))
    return article_helper(inserted_article)


def retrieve_article(id: str, saga: str) -> dict:
    """
    :param saga: one the three sagas
    :param id: id of the desired article
    :return: article info
    """
    article = saga_collections.get(saga).find_one({"_id": ObjectId(id)})
    if article:
        return article_helper(article)


def update_article_data(id: str, saga: str, article_updates: dict) -> bool:
    """
    :param saga:
    :param id: the id of the article
    :param article_updates: all the information related to the article that will be updated
    :return: updated article info
    """
    if len(article_updates) < 1:
        return False
    article =  saga_collections.get(saga).find_one({"_id": ObjectId(id)})
    if article:
        updated_article =  saga_collections.get(saga).update_one(
            {"_id": ObjectId(id)}, {"$set": article_updates}
        )
        if updated_article:
            return True
        return False


def delete_article(id: str, saga: str) -> bool:
    """
    :param saga:
    :param id: the id of the article to be deleted
    :return: deleted article info
    """
    article = saga_collections.get(saga).find_one({"_id": ObjectId(id)})
    if article:
        saga_collections.get(saga).delete_one({"_id": ObjectId(id)})
        return True
    return False


def filter_by_entities_time(saga: str, time_start: int, time_end: int, minimum: int) -> dict:
    """
    :param time_start: the starting time for filtering
    :param time_end: the ending time for filtering
    :param saga: the name of the saga
    :return: entities with their frequency
    """
    entities = []
    for result in saga_collections.get(saga).find({"time": {"$gt": time_start, "$lt": time_end}}):
        entities.extend(result.get("entities"),[""])
    count_elements = Counter(entities)
    frequent_entities, counts = zip(*count_elements.most_common(minimum))
    output = {"time_start": time_start, "time_end": time_end, "entities": entities,
              "reads_each_entity": dict(zip(entities, list(counts)))}
    return output
