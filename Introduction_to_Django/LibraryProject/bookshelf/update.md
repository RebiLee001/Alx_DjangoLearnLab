# Update Operation

**Command:**

```python
from bookshelf.models import Book

# Get the book
book1 = Book.objects.get(title="1984")

# Update title
book1.title = "Nineteen Eighty-Four"
book1.save()

# Check updated book
Book.objects.get(id=book1.id)