from django.urls import path
from users.views import RegisterView, UsersViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
]

router = DefaultRouter()
router.register("", UsersViewSet, basename="users")
urlpatterns += router.urls
