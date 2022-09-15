from http import HTTPStatus

from bson.errors import InvalidId
from fastapi import APIRouter
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder

from models.data_schema import CreditCardResults, UpdateCreditCardResults
from services.credit_card_crud import add_credit_card_doc, get_all_credit_cards, retrieve_credit_card, \
    update_credit_card, delete_credit_card
from utils.helpers import response_model

router = APIRouter()


@router.post("/", response_description="credit card data added into the database")
async def add_credit_card(credit_card: CreditCardResults):
    credit_card = jsonable_encoder(credit_card)
    new_credit_card = await add_credit_card_doc(credit_card)
    return response_model(new_credit_card, "credit card added successfully.")


@router.get("/", response_description="credit card data retrieved")
async def get_all_credit_card_data():
    credit_cards = await get_all_credit_cards()
    if credit_cards:
        return response_model(credit_cards, "credit card data retrieved successfully")
    return response_model(credit_cards, "Empty list returned")


@router.get("/{id}", response_description="credit card data retrieved")
async def get_credit_data(id: str):
    try:
        credit_card = await retrieve_credit_card(id)
    except InvalidId:
        raise HTTPException(status_code=HTTPStatus.UNPROCESSABLE_ENTITY, detail="Id not valid, provide a valid Id")
    if credit_card:
        return response_model(credit_card, "credit card data retrieved successfully")
    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Credit card not found")


@router.put("/{id}")
async def update_credit_card_data(id: str, req: UpdateCreditCardResults) -> object:
    try:
        data = {key: value for key, value in req.dict().items() if value is not None}
        updated_credit_card = await update_credit_card(id, data)
    except InvalidId:
        raise HTTPException(status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
                            detail="Could not update credit card data, Id not valid")
    if updated_credit_card:
        return response_model(
            "credit card with ID: {}  update is successful".format(id),
            "credit card name updated successfully",
        )
    raise HTTPException(status_code=HTTPStatus.CONFLICT, detail="Credit card not found")


@router.delete("/{id}", response_description="credit card deleted from the database")
async def delete_credit_card_data(id: str):
    try:
        deleted_credit_card = await delete_credit_card(id)
    except InvalidId:
        raise HTTPException(status_code=HTTPStatus.UNPROCESSABLE_ENTITY, detail="Id not valid")
    if deleted_credit_card:
        return response_model(
            "credit card with ID: {} removed".format(id), "credit card deleted successfully"
        )
    return HTTPException(status_code=HTTPStatus.CONFLICT, detail="Credit card data not found"
                         )
