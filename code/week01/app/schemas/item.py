"""条目的请求和响应模型。"""

from pydantic import BaseModel, Field


class ItemCreate(BaseModel):
    name: str = Field(min_length=1)
    description: str = ""


class Item(BaseModel):
    id: int
    name: str
    description: str = ""
