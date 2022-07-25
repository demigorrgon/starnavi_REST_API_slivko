from rest_framework.routers import DefaultRouter
from posts.views import LikeAnalyticsViewSet, PostViewset


router = DefaultRouter()
router.register("", PostViewset, basename="posts")
router.register("analytics", LikeAnalyticsViewSet, basename="analytics")
urlpatterns = router.urls
