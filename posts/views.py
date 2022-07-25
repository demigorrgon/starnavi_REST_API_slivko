from django.db import IntegrityError
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from posts.models import Post
from posts.serializers import PostSerializer


class PostViewset(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    http_method_names = ["get", "post", "delete"]

    @action(detail=True, methods=["POST"], permission_classes=[AllowAny])
    def like(self, request, *args, **kwargs):
        post = self.get_object()
        post.likes.add(request.user)
        post.save()

        return Response(
            data={"response": "Post was liked successfully"}, status=status.HTTP_200_OK
        )

    @action(detail=True, methods=["POST"], permission_classes=[AllowAny])
    def dislike(self, request, *args, **kwargs):
        post = self.get_object()
        post.likes.remove(request.user)
        post.save()

        return Response(
            data={"response": "Post was disliked successfully"},
            status=status.HTTP_200_OK,
        )

    def create(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response(
                data={"response": "Authorization token required"},
                status=status.HTTP_403_FORBIDDEN,
            )

        data = request.data
        creator = request.user
        try:
            new_post = Post.objects.create(
                title=data.get("title"), creator=creator, content=data.get("content")
            )
        except IntegrityError:
            return Response(
                data={
                    "response": "Please provide following fields: 'title', 'content'"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = PostSerializer(new_post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        obj_to_delete = self.get_object()
        if request.user.username != obj_to_delete.creator.username:
            return Response(
                data={"response": "You cannot delete someone else's "},
                status=status.HTTP_403_FORBIDDEN,
            )
        self.perform_destroy(obj_to_delete)
        return Response(status=status.HTTP_204_NO_CONTENT)
