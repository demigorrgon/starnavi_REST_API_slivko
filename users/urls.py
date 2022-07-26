from django.urls import path
from users.views import RegisterView, UsersViewSet, UserActivity
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path(
        "user-activity/<int:pk>",
        UserActivity.as_view(),
        name="user-activity",
    ),
]

router = DefaultRouter()
router.register("", UsersViewSet, basename="users")
urlpatterns += router.urls
