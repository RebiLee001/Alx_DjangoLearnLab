from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book

# View for listing books (requires can_view permission)
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

# Example view for creating a book (requires can_create permission)
@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    # You can implement a form here later
    return render(request, 'bookshelf/book_create.html')
