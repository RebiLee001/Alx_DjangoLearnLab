from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


# ----------------------------
# List all books (READ ONLY)
# Accessible to everyone, with filtering, searching, and ordering
# ----------------------------
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Fields allowed for filtering
    filterset_fields = ['title', 'publication_year', 'author']

    # Fields allowed for searching
    search_fields = ['title', 'author__name']

    # Fields allowed for ordering
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']


# ----------------------------
# Retrieve single book by ID
# Accessible to everyone
# ----------------------------
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# ----------------------------
# Create a new book
# Authenticated users only
# ----------------------------
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# ----------------------------
# Update an existing book
# Authenticated users only
# ----------------------------
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# ----------------------------
# Delete a book
# Authenticated users only
# ----------------------------
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

