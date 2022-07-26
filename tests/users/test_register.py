import pytest
from django.urls import reverse

from users.serializers import UserSerializer

pytestmark = [pytest.mark.django_db]


def test_register_user(anon_api_client):
    url = reverse("register")
    response = anon_api_client.post(
        url,
        {
            "username": "kabob33",
            "email": "some@i.com",
            "password": "wasdaqwe",
            "first_name": "ka",
            "last_name": "bob",
        },
        format="json",
    )
    assert response.status_code == 201


def test_register_existing_user(anon_api_client, dummy_user):
    url = reverse("register")
    response = anon_api_client.post(url, UserSerializer(dummy_user).data, format="json")
    assert response.status_code == 400
