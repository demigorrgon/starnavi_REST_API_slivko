from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
)
from posts.models import Like, Post


class LikeSerializer(ModelSerializer):
    # liked_by = ReadOnlyField(source="like.liked_by")
    liked_by = SerializerMethodField()

    class Meta:
        fields = ("liked_by", "liked_at")
        model = Like

    def get_liked_by(self, obj):
        return obj.liked_by.username


class PostSerializer(ModelSerializer):
    likes = LikeSerializer(source="like_set", read_only=True, many=True)
    creator = SerializerMethodField()
    created_at = SerializerMethodField()

    class Meta:
        fields = ("id", "title", "creator", "content", "created_at", "likes")
        model = Post

    def get_creator(self, obj):
        return obj.creator.username

    def get_created_at(self, obj):
        return obj.created_at.strftime("%d-%m-%Y %H:%M %Z")
