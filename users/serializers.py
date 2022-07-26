from rest_framework.serializers import ModelSerializer
from users.models import BaseUser
from posts.serializers import PostSerializer


class UserSerializer(ModelSerializer):
    posts = PostSerializer(read_only=True, many=True)

    class Meta:
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "last_login",
            "last_activity",
            "posts",
        )
        model = BaseUser


class UserActivitySerializer(UserSerializer):
    class Meta:
        fields = ("username", "last_login", "last_activity")
        model = BaseUser
