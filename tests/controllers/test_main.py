from fastapi.testclient import TestClient
from server import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "Welocome to store dashboard" in response.text
    # assert response.content == ""