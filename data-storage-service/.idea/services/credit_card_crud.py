from typing import List

from bson.errors import InvalidId
from bson.objectid import ObjectId

from database.DB import credit_card_collection
from utils.helpers import credit_card_helper


async def get_all_credit_cards() -> List:
    """
    :return: list of  all the credit cards data
    """
    credit_cards = []
    async for result in credit_card_collection.find():
        result['_id'] = str(result['_id'])
        credit_cards.append(result)
    return credit_cards


async def add_credit_card_doc(credit_card_data: dict) -> dict:
    """
    :param credit_card_data: all the information related to the credit card that will be inserted to the database
    :return: inserted credit card info
    """
    credit_card = await credit_card_collection.insert_one(credit_card_data)
    inserted_credit_card = await credit_card_collection.find_one({"_id": credit_card.inserted_id})
    return credit_card_helper(inserted_credit_card)


async def retrieve_credit_card(id: str) -> dict:
    """
    :param id: id of the desired credit card
    :return: credit card info
    """
    credit_card = await credit_card_collection.find_one({"_id": ObjectId(id)})
    if credit_card:
        return credit_card_helper(credit_card)


async def update_credit_card(id: str, data: dict) -> bool:
    """
    :param id: the id of the credit card
    :param data: all the information related to the credit card that will be updated to the database
    :return: inserted credit card info
    """
    if len(data) < 1:
        return False
    credit_card = await credit_card_collection.find_one({"_id": ObjectId(id)})
    if credit_card:
        updated_credit_card = await credit_card_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_credit_card:
            return True
        return False


async def delete_credit_card(id: str) -> bool:
    """
    :param id: the id of the credit card to be deleted
    :return: deleted credit card info
    """
    credit_card = await credit_card_collection.find_one({"_id": ObjectId(id)})
    if credit_card:
        await credit_card_collection.delete_one({"_id": ObjectId(id)})
        return True
    return False
