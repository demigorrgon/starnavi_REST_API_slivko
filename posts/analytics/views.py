from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from posts.serializers import LikeSerializer
from posts.models import Like
from datetime import datetime


class LikeAnalyticsViewSet(ModelViewSet):
    http_method_names = ["get"]
    serializer_class = LikeSerializer

    def get_queryset(self):
        # django-filter prob would be better
        date_from = self.request.query_params.get("date_from")
        date_to = self.request.query_params.get("date_to")
        if date_from and date_to:
            likes_between_provided_dates = Like.objects.filter(
                liked_at__date__range=(
                    datetime.strptime(date_from, "%Y-%m-%d"),
                    datetime.strptime(date_to, "%Y-%m-%d"),
                )
            )
            return likes_between_provided_dates

    def list(self, request, *args, **kwargs):
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
