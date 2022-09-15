from typing import Optional

from pydantic import BaseModel, Field, EmailStr


class CreditCardResults(BaseModel):
    credit_card_holder: str = Field(description="the name of the credit card holder")
    bank: str = Field(description="the name of the issuing bank")
    date_of_expiry: str = Field(description="date of expiry")

    class Config:
        schema_extra = {
            "example": {
                "credit_card_holder": "Jane Smith",
                "bank": "credit agricole",
                "date_of_expiry": "26/09/22",
            }
        }


class UpdateCreditCardResults(BaseModel):
    credit_card_holder: Optional[str]
    bank: Optional[str]
    date_of_expiry: Optional[str]

