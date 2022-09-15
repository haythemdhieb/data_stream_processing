def article_helper(article) -> dict:
    return {
        "id": str(article.get("_id", "")),
        "time": article.get("time", ""),
        "text": article.get("text", ""),
        "entities": article.get("entities", [""]),
        "saga": article.get("saga", "")
    }


def response_model(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }
