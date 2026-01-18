# Retrieve Operation

**Command:**

```python
from bookshelf.models import Book

# Retrieve the book we just created
book1 = Book.objects.get(title="1984")
book1
