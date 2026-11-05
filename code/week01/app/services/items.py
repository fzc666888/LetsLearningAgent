"""条目的内存存储。"""

from app.schemas.item import Item, ItemCreate

_items: dict[int, Item] = {}
_next_id: int = 1


class ItemNotFoundError(Exception):
    """按 id 找不到条目。"""


def reset_items() -> None:
    """清空内存数据，供测试在每个用例前调用。"""
    global _next_id
    _items.clear()
    _next_id = 1


def create_item(payload: ItemCreate) -> Item:
    global _next_id
    item = Item(id=_next_id, name=payload.name, description=payload.description)
    _items[item.id] = item
    _next_id += 1
    return item


def list_items() -> list[Item]:
    return [_items[item_id] for item_id in sorted(_items)]


def get_item(item_id: int) -> Item:
    item = _items.get(item_id)
    if item is None:
        raise ItemNotFoundError(item_id)
    return item


def update_item(item_id: int, payload: ItemCreate) -> Item:
    current = get_item(item_id)
    updated = Item(id=current.id, name=payload.name, description=payload.description)
    _items[item_id] = updated
    return updated


def delete_item(item_id: int) -> None:
    get_item(item_id)
    del _items[item_id]
