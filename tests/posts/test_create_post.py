from posts.models import Post
import pytest

pytestmark = [pytest.mark.django_db]


def test_post_fixture(dummy_post):
    assert dummy_post.content is not None


def test_manually_create_post(dummy_user):
    post = Post(title="wasda", creator=dummy_user, content="asd123")
    post.save()
    created_post = Post.objects.select_related("creator").get(title="wasda")
    assert created_post.creator == dummy_user
