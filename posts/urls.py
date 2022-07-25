from rest_framework.routers import DefaultRouter
from posts.views import PostViewset


router = DefaultRouter()
router.register("", PostViewset, basename="posts")
urlpatterns = router.urls
