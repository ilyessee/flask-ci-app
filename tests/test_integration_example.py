import pytest

from app import create_app


@pytest.fixture()
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


class TestHealthEndpoint:
    def test_health_returns_200(self, client):
        response = client.get("/health")
        assert response.status_code == 200

    def test_health_returns_ok_status(self, client):
        data = response = client.get("/health")
        data = response.get_json()
        assert data["status"] == "ok"


class TestIndexEndpoint:
    def test_index_returns_200(self, client):
        response = client.get("/")
        assert response.status_code == 200

    def test_index_contains_items_heading(self, client):
        response = client.get("/")
        assert b"Items" in response.data


class TestAddItem:
    def test_add_item_redirects(self, client):
        response = client.post("/add", data={"item": "test-item"})
        assert response.status_code == 302

    def test_add_empty_item_still_redirects(self, client):
        response = client.post("/add", data={"item": ""})
        assert response.status_code == 302
