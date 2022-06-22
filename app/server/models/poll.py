import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field


class PollSchema(BaseModel):
    title: str = Field(...)
    description: str = Field(...)
    length: int = Field(..., gt=0 , lte= 4)
    options: dict = Field(...)


    class Config:
        schema_extra = {
            "example": {
                "title": "John Doe",
                "description": "Water resources and environmental engineering",
                "length": 4,
                "createdDate": datetime.datetime.now(),
                "updatedDate": datetime.datetime.now(),
                "options": {'option': 1}
            }
        }
class UpdatePollModel(BaseModel):
    title: Optional[str]
    description: Optional[str]
    length: Optional[int]
    createdDate: Optional[datetime.datetime]
    updatedDate: datetime.datetime = Field(...)
    options: Optional[dict]

    class Config:
        schema_extra = {
            "example": {
                "title": "John Doe",
                "description": "water resources and environmental engineering",
                "length": 3,
                "createdDate": datetime.datetime.now(),
                "updatedDate": datetime.datetime.now(),
                "options": {'option': 1}
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
