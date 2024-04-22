from urllib.parse import urlparse
from fastapi.testclient import TestClient
from server import app

client = TestClient(app)

def test_login_page_render():
    response = client.get("/login")
    assert response.status_code == 200
    assert "username" in response.text
    assert "password" in response.text

def test_login_correct_form_submit():
    res = client.post("/login", data={"username":"tarek", "password": "t123"})
    assert res.status_code == 200
    assert "logout" in res.text
    assert res.url.path == "/"

def test_login_wrong_username_form_submit():
    res = client.post("/login", data={"username":"asdfasdf", "password": "123456"})
    assert res.status_code == 401
    assert "Wrong username or password" in res.text

def test_login_wrong_password_form_submit():
    res = client.post("/login", data={"username":"tarek", "password": "123456"})
    assert res.status_code == 401
    assert "Wrong username or password" in res.text


def test_logout_after_login():
    test_login_correct_form_submit()
    res = client.get("/logout")
    assert res.status_code == 200
    assert "login" in res.text
    assert res.url.path == "/"