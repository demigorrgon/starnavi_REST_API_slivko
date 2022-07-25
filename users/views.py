from django.db import IntegrityError
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from users.models import BaseUser
from users.serializers import UserSerializer


class RegisterView(CreateAPIView):
    queryset = BaseUser.objects.all()
    serializer_class = UserSerializer()

    def create(self, request, *args, **kwargs):
        data = request.data
        try:
            user = BaseUser.objects.create_user(
                email=data.get("email"),
                username=data.get("username"),
                password=data.get("password"),
                first_name=data.get("first_name"),
                last_name=data.get("last_name"),
            )
        except ValueError:
            return Response(
                {
                    "response": "Please provide valid fields: email, username, password, first_name, last_name"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        except IntegrityError:
            return Response(
                {"response": "User already exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UsersViewSet(ModelViewSet):
    queryset = BaseUser.objects.all()
    serializer_class = UserSerializer
    http_method_names = ["get", "patch", "options"]
