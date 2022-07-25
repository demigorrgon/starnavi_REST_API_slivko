from rest_framework.serializers import ModelSerializer
from posts.models import Like, Post


class LikeSerializer(ModelSerializer):
    class Meta:
        fields = ("__all__",)
        model = Like


class PostSerializer(ModelSerializer):
    likes = LikeSerializer(read_only=True, many=True)

    class Meta:
        fields = ("id", "title", "creator", "content", "created_at", "likes")
        model = Post
