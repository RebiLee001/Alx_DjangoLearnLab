from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from .views import FeedView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    *router.urls,
    path('feed/', FeedView.as_view(), name='feed'),
]