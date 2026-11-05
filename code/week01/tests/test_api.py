import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.services.items import reset_items


@pytest.fixture
def client() -> TestClient:
    reset_items()
    return TestClient(app)


def test_health(client: TestClient) -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_item(client: TestClient) -> None:
    response = client.post(
        "/items",
        json={"name": "笔记", "description": "第一篇"},
    )
    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "笔记", "description": "第一篇"}


def test_list_items(client: TestClient) -> None:
    client.post("/items", json={"name": "笔记", "description": "第一篇"})
    client.post("/items", json={"name": "草稿"})
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "name": "笔记", "description": "第一篇"},
        {"id": 2, "name": "草稿", "description": ""},
    ]


def test_read_item(client: TestClient) -> None:
    client.post("/items", json={"name": "笔记", "description": "第一篇"})
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json()["name"] == "笔记"


def test_update_item(client: TestClient) -> None:
    client.post("/items", json={"name": "笔记", "description": "第一篇"})
    response = client.put(
        "/items/1",
        json={"name": "笔记修订", "description": "改过"},
    )
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "笔记修订", "description": "改过"}


def test_delete_item(client: TestClient) -> None:
    client.post("/items", json={"name": "笔记", "description": "第一篇"})
    response = client.delete("/items/1")
    assert response.status_code == 200
    assert response.json() == {"status": "deleted"}
    assert client.get("/items").json() == []


def test_read_missing_item(client: TestClient) -> None:
    response = client.get("/items/99")
    assert response.status_code == 404
    assert response.json()["detail"] == "条目不存在"
