from http import HTTPStatus

from bson.errors import InvalidId
from fastapi import APIRouter
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder

from models.data_schema import Article, UpdatedArticle, TimeInterval
from services.articles_crud import add_article_data, get_all_articles, retrieve_article, delete_article, \
    filter_by_entities_time, update_article_data
from utils.helpers import response_model

router = APIRouter()


@router.post("/", response_description="Article data added into the database")
async def add_article(saga: str, article: Article):
    article = add_article_data(saga,article.dict())
    print(article)
    return response_model(article, "Article added successfully.")


@router.get("/", response_description="Articles data retrieved")
async def get_all_articles_data(saga: str):
    articles =  get_all_articles(saga)
    print(articles)
    if articles:
        return response_model(articles, "articles data retrieved successfully")
    return response_model(articles, "Empty list returned")


@router.get("/{id}", response_description="Articles data retrieved")
async def get_article(id: str, saga: str):
    try:
        article = await retrieve_article(id, saga)
    except InvalidId:
        raise HTTPException(status_code=HTTPStatus.UNPROCESSABLE_ENTITY, detail="Id not valid, provide a valid Id")
    if article:
        return response_model(article, "Article data retrieved successfully")
    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Article not found")


@router.put("/{id}")
async def update_article(id: str, saga: str, req: UpdatedArticle) -> object:
    try:
        data = {key: value for key, value in req.dict().items() if value is not None}
        updated_article = await update_article_data(id, saga, data)
    except InvalidId:
        raise HTTPException(status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
                            detail="Could not update article data, Id not valid")
    if updated_article:
        return response_model(
            "Article with ID: {}  update is successful".format(id),
            "Article name updated successfully",
        )
    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Article not found")


@router.delete("/{id}", response_description="Article deleted from the database")
async def delete_article_data(id: str, saga: str):
    try:
        deleted_article = await delete_article(id, saga)
    except InvalidId:
        raise HTTPException(status_code=HTTPStatus.UNPROCESSABLE_ENTITY, detail="Id not valid")
    if deleted_article:
        return response_model(
            "Article with ID: {} removed".format(id), "Article deleted successfully"
        )
    return HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Article data not found"
                         )


@router.post("/filter", response_description="Filter articles")
async def filter_article_data(saga: str, minimum_readers: int, time_interval: TimeInterval):
    articles = filter_by_entities_time(saga, time_interval.dict().get("time_start"), time_interval.dict().get("time_end"),
                                             minimum_readers)
    if articles:
        return response_model(articles, "Articles found for saga {}".format(saga))

    return HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Article within this time range are not found"
                         )
