# query_samples.py
from relationship_app.models import Author, Book, Library, Librarian

# 1. Create sample data
author1 = Author.objects.create(name="George Orwell")
book1 = Book.objects.create(title="1984", author=author1)
book2 = Book.objects.create(title="Animal Farm", author=author1)

library1 = Library.objects.create(name="Central Library")
library1.books.add(book1, book2)

librarian1 = Librarian.objects.create(name="Alice Johnson", library=library1)

# 2. Query all books by a specific author
books_by_orwell = Book.objects.filter(author__name="George Orwell")
print("Books by George Orwell:", list(books_by_orwell))

# 3. List all books in a library
books_in_library = library1.books.all()
print("Books in Central Library:", list(books_in_library))

# 4. Retrieve the librarian for a library
library_librarian = library1.librarian
print("Librarian of Central Library:", library_librarian)
