import datetime
from typing import Dict, Optional

from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field


class UserSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    createdDate: datetime.datetime = Field(...)
    updatedDate: datetime.datetime = Field(...)


    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "email": "jdoe@x.edu.ng",
                "password": "Water resources engineering",
                "createdDate": datetime.datetime.now(),
                "updatedDate": datetime.datetime.now(),
            }
        }


class UpdateUserModel(BaseModel):
    fullname: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]
    createdDate: Optional[datetime.datetime]
    updatedDate: datetime.datetime = Field(...)
    options: Optional[Dict] = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "email": "jdoe@x.edu.ng",
                "password": "Water resources and environmental engineering",
                "createdDate": datetime.datetime.now(),
                "updatedDate": datetime.datetime.now(),
                "options": {
                    "option1": "option1",
                    "option2": "option2",
                    "option3": "option3",
                },
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