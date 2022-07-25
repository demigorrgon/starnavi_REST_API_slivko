from datetime import datetime
from django.db import IntegrityError
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from posts.models import Like, Post
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


class LikeAnalyticsViewSet(ModelViewSet):
    http_method_names = ["get"]

    def get_queryset(self):
        # django-filter prob would be better
        date_from = self.request.query_params.get("date_from")
        date_to = self.request.query_params.get("date_to")
        if date_from and date_to:
            likes_between_provided_dates = Like.objects.filter(
                created_at__date__range=(
                    datetime.strptime(date_from, "%Y-%M-%d"),
                    datetime.strptime(date_to, "%Y-%M-%d"),
                )
            )
            print(likes_between_provided_dates)
            return likes_between_provided_dates
        # return Response(
        #     data={
        #         "response": "Please provide 'date_from' and 'date_to' query parameters (in url)"
        #     },
        #     status=status.HTTP_400_BAD_REQUEST,
        # )

    def detail(self, request, *args, **kwargs):
        likes_in_date_range = self.get_queryset()
        if not likes_in_date_range:
            return Response(
                data={
                    "response": "There are no likes in that time period, are provided dates correct?"
                },
                status=status.HTTP_200_OK,
            )

        return Response(
            data={
                "response": f"There was {likes_in_date_range.count()} likes in that timespan"
            },
            status=status.HTTP_200_OK,
        )
