import pytest
from django.test import Client
from rest_framework import status


@pytest.mark.django_db
def test_account():
    client = Client()
    response = client.get('/account/account/')
    assert response.status_code == status.HTTP_200_OK, response.content
