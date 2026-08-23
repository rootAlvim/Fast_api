from tests.conftest import client
from http import HTTPStatus

def test_create_user(client): #POST
    response = client.post('/users/', json={
        'username': 'alice',
        'email': 'alice@gmail.com',
        'password': '123',

    })
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'alice',
        'email': 'alice@gmail.com',
        'id': 1,
    }

def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
        ]
    }

