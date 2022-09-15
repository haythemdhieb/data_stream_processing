from enum import Enum
from typing import List
from typing import Optional

from pydantic import BaseModel
from pydantic import Field


class Sagas(str, Enum):
    lotr = 'lotr'
    got = 'got'
    hp = 'hp'


class Article(BaseModel):
    saga: Sagas = Field(description="the name of the saga")
    text: str = Field(description="the text within the article")
    entities: List[str] = Field(description="the entities within the article")
    time: int = Field(description="the time of which the article is streamed")

    class Config:
        use_enum_values = True

    class Config:
        schema_extra = {
            "example": {
                "saga": "got",
                "text": "Denerys Targeryane",
                "entities": ["Denerys"],
                "time": "15478",
            }
        }


class UpdatedArticle(BaseModel):
    saga: Optional[str]
    text: Optional[str]
    time: Optional[int]


class TimeInterval(BaseModel):
    time_start: int = Field(description="the starting time")
    time_end: int = Field(description="the ending time")
