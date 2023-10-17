import pytest
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient


@pytest.fixture
def create_test_data():
    User.objects.create(username='stas', password='stas1234', email='stas@example.com')


@pytest.mark.django_db
def test_create_book_api_view_404(create_test_data):
    client = APIClient()

    data = {
        'title': 'Test Book',
        'author': 1,
        'year_published': 2023,
        'short_description': 'Short description for test book',
        'full_description': 'Full description for test book',
        'last_read_date': '2023-10-18'
    }

    url = 'http://127.0.0.1:8000/api/bookkk/'
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_book_detail_view_404(create_test_data):
    client = APIClient()

    url = 'http://127.0.0.1:8000/api/book_detail/131232'

    response = client.get(url, follow=True)

    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_book_detail_view_401(create_test_data):
    client = APIClient()

    url = 'http://127.0.0.1:8000/api/book_detail/1'

    response = client.get(url, follow=True)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_book_list_view_404(create_test_data):
    client = APIClient()
    url = 'http://127.0.0.1:8000/api/book_detail_listt'

    response = client.get(url, follow=True)

    assert response.status_code == status.HTTP_404_NOT_FOUND

