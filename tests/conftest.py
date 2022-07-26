import pytest
from mixer.backend.django import mixer
from posts.models import Post
from rest_framework.test import APIClient
from django.urls import reverse

from users.models import BaseUser


@pytest.fixture
def dummy_user(django_user_model):
    """
    mixer is a package similar to factory_boy that generates random data in provided model fields
    returns randomized instance of a user model
    """
    return mixer.blend(django_user_model)


@pytest.fixture
def dummy_post():
    return mixer.blend(Post)


@pytest.fixture
def test_user():
    user = BaseUser.objects.create_user(
        username="kabob",
        email="k@gmail.com",
        password="verysecurepass",
        first_name="ka",
        last_name="bob",
    )
    return user


@pytest.fixture
def users_post(test_user):
    post = Post.objects.create(title="some", creator=test_user, content="something")
    return post


@pytest.fixture
def anon_api_client():
    client = APIClient()
    return client


@pytest.fixture
def token(anon_api_client, test_user):
    url = reverse("obtain-token")
    return anon_api_client.post(
        url, {"username": test_user.username, "password": "verysecurepass"}
    ).data["access"]


@pytest.fixture
def api_client_with_token(token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    return client
