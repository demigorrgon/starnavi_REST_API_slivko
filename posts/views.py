from django.db import IntegrityError
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import action
from posts.models import Post
from posts.serializers import PostSerializer


class PostViewset(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "delete"]

    @action(
        detail=True,
        methods=["POST"],
        permission_classes=[IsAuthenticated],
        url_name="like",
    )
    def like(self, request, *args, **kwargs):
        post = self.get_object()
        post.likes.add(request.user)
        post.save()

        return Response(
            data={"response": "Post was liked successfully"}, status=status.HTTP_200_OK
        )

    @action(
        detail=True,
        methods=["POST"],
        permission_classes=[IsAuthenticated],
        url_name="dislike",
    )
    def dislike(self, request, *args, **kwargs):
        post = self.get_object()
        post.likes.remove(request.user)
        post.save()

        return Response(
            data={"response": "Post was disliked successfully"},
            status=status.HTTP_200_OK,
        )

    def create(self, request, *args, **kwargs):
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
                data={"response": "You cannot delete someone else's post"},
                status=status.HTTP_403_FORBIDDEN,
            )
        self.perform_destroy(obj_to_delete)
        return Response(status=status.HTTP_204_NO_CONTENT)
