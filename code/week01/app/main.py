"""内存版条目 API：/health 与 /items 的增删改查。"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="LearningAgent")


class ItemCreate(BaseModel):
    name: str = Field(min_length=1)
    description: str = ""


class Item(BaseModel):
    id: int
    name: str
    description: str = ""


_items: dict[int, Item] = {}
_next_id: int = 1


def _get_item_or_404(item_id: int) -> Item:
    item = _items.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="条目不存在")
    return item


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/items", status_code=201)
def create_item(payload: ItemCreate) -> Item:
    global _next_id
    item = Item(id=_next_id, name=payload.name, description=payload.description)
    _items[item.id] = item
    _next_id += 1
    return item


@app.get("/items")
def list_items() -> list[Item]:
    return [_items[item_id] for item_id in sorted(_items)]


@app.get("/items/{item_id}")
def read_item(item_id: int) -> Item:
    return _get_item_or_404(item_id)


@app.put("/items/{item_id}")
def update_item(item_id: int, payload: ItemCreate) -> Item:
    current = _get_item_or_404(item_id)
    updated = Item(id=current.id, name=payload.name, description=payload.description)
    _items[item_id] = updated
    return updated


@app.delete("/items/{item_id}")
def delete_item(item_id: int) -> dict[str, str]:
    _get_item_or_404(item_id)
    del _items[item_id]
    return {"status": "deleted"}
