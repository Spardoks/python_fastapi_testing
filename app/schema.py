import datetime
from typing import Optional

from pydantic import BaseModel


class IdResponse(BaseModel):
    id: int


class CreateAdvertismentRequest(BaseModel):
    title: str
    description: str
    author: str
    price: str


class CreateAdvertismentResponse(IdResponse):
    pass


class GetAdvertismentResponse(BaseModel):
    id: int
    title: str
    description: str
    author: str
    price: str
    created_at: datetime.datetime


class UpdateAdvertismentRequest(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    author: Optional[str] = None
    price: Optional[str] = None


class UpdateAdvertismentResponse(IdResponse):
    pass
