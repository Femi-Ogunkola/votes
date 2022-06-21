import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field


class PollSchema(BaseModel):
    title: str = Field(...)
    description: str = Field(...)
    style: str = Field(...)
    #createdDate: datetime.datetime = Field(...)
    #updatedDate: datetime.datetime = Field(...)


    class Config:
        schema_extra = {
            "example": {
                "title": "John Doe",
                "description": "Water resources and environmental engineering",
                "style": 'rank',
                "createdDate": datetime.datetime.now(),
                "updatedDate": datetime.datetime.now(),
            }
        }
class UpdatePollModel(BaseModel):
    title: Optional[str]
    description: Optional[str]
    style: Optional[str]
    createdDate: Optional[datetime.datetime]
    updatedDate: datetime.datetime = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "title": "John Doe",
                "description": "water resources and environmental engineering",
                "style": 'options',
                "createdDate": datetime.datetime.now(),
                "updatedDate": datetime.datetime.now(),
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
