from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import BookList, BookViewSet


router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')


urlpatterns = [
    # Token authentication endpoint
    path('token/', obtain_auth_token, name='api-token'),

    # ListAPIView
    path('books/', BookList.as_view(), name='book-list'),

    # CRUD routes
    path('', include(router.urls)),
]
