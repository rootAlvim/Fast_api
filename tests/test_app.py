'''from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_home_status_ok():
    response = client.get("/")
    assert response.status_code == 200
'''
from http import HTTPStatus
from fastapi.testclient import TestClient
from fast_zero.app import app

def test__root():
    client = TestClient(app)
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}