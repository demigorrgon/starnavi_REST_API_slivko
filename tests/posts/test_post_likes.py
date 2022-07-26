import pytest
from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def test_like_post_by_anonymous_user(anon_api_client, dummy_post):
    assert isinstance(dummy_post.content, str)
    url = reverse("posts-like", kwargs={"pk": dummy_post.pk})
    response = anon_api_client.post(url)

    assert response.status_code == 401


def test_like_post_by_authorized_user(api_client_with_token, dummy_post):
    url = reverse("posts-like", kwargs={"pk": dummy_post.pk})
    response = api_client_with_token.post(url)

    assert response.status_code == 200


def test_dislike_post_by_anonymous_user(anon_api_client, dummy_post):
    url = reverse("posts-dislike", kwargs={"pk": dummy_post.pk})
    response = anon_api_client.post(url)

    assert response.status_code == 401


def test_dislike_post_by_authorized_user(api_client_with_token, dummy_post):
    url = reverse("posts-dislike", kwargs={"pk": dummy_post.pk})
    response = api_client_with_token.post(url)

    assert response.status_code == 200
