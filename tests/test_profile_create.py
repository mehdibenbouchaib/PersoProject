import pytest
from rest_framework import status
from rest_framework.test import APIClient

client = APIClient()


@pytest.mark.django_db
def teste_profile_create():

    pyload = dict(
        name="oussama",
        email="youn@test.com",
        age=25
    )

    response = client.post("/profile/profile/", pyload)
    data = response.data
    assert response.status_code == status.HTTP_201_CREATED, response.content


@pytest.mark.django_db
def teste_profile_create_when_enter_inferior_than_18():
    client.force_authenticate()

    pyload = dict(
        name="oussama",
        email="youn@test.com",
        age=17
    )

    response = client.post("/profile/profile/", pyload)
    data = response.data

    assert response.status_code == status.HTTP_400_BAD_REQUEST, response.content





