from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from rest_framework.schemas import get_schema_view
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/token/", TokenObtainPairView.as_view(), name="obtain-token"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh-token"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="verify-token"),
    path("api/posts/", include("posts.urls")),
    path("api/users/", include("users.urls")),
    path("api/analytics/", include("posts.analytics.urls")),
    path(
        "schema",
        get_schema_view(
            title="lannister",
            description="api schema",
            version="1.0.0",
        ),
        name="openapi_schema",
    ),
    path("docs/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]
