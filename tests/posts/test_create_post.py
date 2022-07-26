import pytest
from django.urls import reverse

from posts.models import Post

pytestmark = [pytest.mark.django_db]


def test_post_fixture(dummy_post):
    assert isinstance(dummy_post.content, str)


def test_manually_create_post(dummy_user):
    post = Post(title="wasda", creator=dummy_user, content="asd123")
    post.save()
    created_post = Post.objects.select_related("creator").get(title="wasda")
    assert created_post.creator == dummy_user


def test_create_post_by_anonymous_user(anon_api_client):
    url = reverse("posts-list")
    response = anon_api_client.post(
        url,
        {
            "title": "let me in",
            "content": "LET ME IN",
        },
        format="json",
    )
    assert response.status_code == 401


def test_create_post_by_authorized_user(api_client_with_token):
    url = reverse("posts-list")
    response = api_client_with_token.post(
        url,
        {
            "title": "let me in",
            "content": "LET ME IN",
        },
        format="json",
    )
    assert response.status_code == 201
