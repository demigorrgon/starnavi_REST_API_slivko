from rest_framework.routers import DefaultRouter

from posts.analytics.views import LikeAnalyticsViewSet

router = DefaultRouter()
router.register("", LikeAnalyticsViewSet, basename="analytics")
urlpatterns = router.urls
