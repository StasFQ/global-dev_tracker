import pytest
from rest_framework import status
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_create_user_api_view_201():
    client = APIClient()

    data = {
        'username': 'test_user',
        'password': 'test_password',
        'email': 'test@test.com',
        'first_name': 'Test',
        'last_name': 'User'
    }


    url = 'http://127.0.0.1:8000/api/authentification/'

    response = client.post(url, data, format='json')

    assert response.status_code == status.HTTP_201_CREATED

    assert 'username' in response.data
    assert 'email' in response.data
    assert 'first_name' in response.data
    assert 'last_name' in response.data


@pytest.mark.django_db
def test_create_user_api_view_404():
    client = APIClient()

    data = {
        'username': 'test_user',
        'password': 'test_password',
        'email': 'test@test.com',
        'first_name': 'Test',
        'last_name': 'User'
    }


    url = 'http://127.0.0.1:8000/api/authentificationnnnn/'

    response = client.post(url, data, format='json')

    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_create_user_api_view_403():
    client = APIClient()

    data = {
    }


    url = 'http://127.0.0.1:8000/api/authentification/'

    response = client.post(url, data, format='json')

    assert response.status_code == status.HTTP_400_BAD_REQUEST
