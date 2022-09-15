def credit_card_helper(credit_card_result) -> dict:
    return {
        "credit_card_holder": credit_card_result.get("credit_card_holder", ""),
        "bank": credit_card_result.get("bank", ""),
        "date_of_expiry": credit_card_result.get("date_of_expiry", ""),
    }


def response_model(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }
