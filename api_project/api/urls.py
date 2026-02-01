from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet


router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')


urlpatterns = [
    # Route for the BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),

    # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),
]
