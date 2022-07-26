from django.urls import reverse
import pytest

pytestmark = [pytest.mark.django_db]


def test_users_list(api_client_with_token):
    url = reverse("users-list")
    response = api_client_with_token.get(url)
    assert response.status_code == 200
