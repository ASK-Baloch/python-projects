from fastapi.testclient import TestClient
from main import app  # Import your FastAPI app

client = TestClient(app)


def test_create_todo():
    response = client.post(
        "/todos/",
        json={
            "title": "Test Todo",
            "description": "This is a test todo item."
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Todo"
    assert data["description"] == "This is a test todo item."


def test_create_todo_validation_error():
    response = client.post(
        "/todos/",
        json={
            "title": 123,  # Intentionally incorrect type
            "description": True  # Intentionally incorrect type
        },
    )
    assert response.status_code == 422  # 422 Unprocessable Entity
