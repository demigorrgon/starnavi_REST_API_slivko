import pytest
from mixer.backend.django import mixer
from posts.models import Post
from rest_framework.test import APIClient


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
def api_client():
    client = APIClient()
    return client
