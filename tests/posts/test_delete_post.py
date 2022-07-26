import pytest
from django.urls import reverse

pytestmark = [pytest.mark.django_db]


def test_delete_post_anon_user(anon_api_client):
    url = reverse("posts-detail", kwargs={"pk": 7})
    response = anon_api_client.delete(url)
    assert response.status_code == 401


def test_delete_post_authorized_user(api_client_with_token, users_post):
    url = reverse("posts-detail", args=[f"{users_post.pk}"])
    response = api_client_with_token.delete(url)
    assert response.status_code == 204


def test_delete_other_users_post(api_client_with_token, dummy_post):
    url = reverse("posts-detail", args=[f"{dummy_post.pk}"])
    response = api_client_with_token.delete(url)
    assert response.status_code == 403
