## 4️⃣ `delete.md`

```markdown
# Delete Operation

**Command:**

```python
from bookshelf.models import Book

# Get the book
book1 = Book.objects.get(title="Nineteen Eighty-Four")

# Delete it
book1.delete()

# Confirm deletion
Book.objects.all()