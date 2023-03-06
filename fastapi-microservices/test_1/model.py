# pydanctic model class for validating data inputs

from pydantic import BaseModel
class test_1(BaseModel):
    """ this pydantic model accepts only 2 fields"""
    id: int
    item: str