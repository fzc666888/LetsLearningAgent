"""条目的增删改查。"""

from fastapi import APIRouter, HTTPException

from app.schemas.item import Item, ItemCreate
from app.services.items import (
    ItemNotFoundError,
    create_item,
    delete_item,
    get_item,
    list_items,
    update_item,
)

router = APIRouter(tags=["items"])


def _item_or_404(item_id: int) -> Item:
    try:
        return get_item(item_id)
    except ItemNotFoundError:
        raise HTTPException(status_code=404, detail="条目不存在") from None


@router.post("/items", status_code=201)
def create_item_route(payload: ItemCreate) -> Item:
    return create_item(payload)


@router.get("/items")
def list_items_route() -> list[Item]:
    return list_items()


@router.get("/items/{item_id}")
def read_item(item_id: int) -> Item:
    return _item_or_404(item_id)


@router.put("/items/{item_id}")
def update_item_route(item_id: int, payload: ItemCreate) -> Item:
    try:
        return update_item(item_id, payload)
    except ItemNotFoundError:
        raise HTTPException(status_code=404, detail="条目不存在") from None


@router.delete("/items/{item_id}")
def delete_item_route(item_id: int) -> dict[str, str]:
    try:
        delete_item(item_id)
    except ItemNotFoundError:
        raise HTTPException(status_code=404, detail="条目不存在") from None
    return {"status": "deleted"}
