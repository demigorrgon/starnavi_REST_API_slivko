"""social_network_core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
