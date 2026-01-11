# LibraryProject

## Overview
LibraryProject is a Django project designed to manage a collection of books. It includes a `bookshelf` app, which contains a `Book` model and demonstrates CRUD operations (Create, Retrieve, Update, Delete) using Django’s ORM and admin interface.

---

## Project Structure

LibraryProject/
├── manage.py
├── LibraryProject/
│ ├── settings.py
│ ├── urls.py
│ └── ...
└── bookshelf/
├── admin.py
├── apps.py
├── models.py
├── views.py
├── migrations/
└── create.md
└── retrieve.md
└── update.md
└── delete.md


---

## Bookshelf App

- **Model:** `Book`
- **Fields:**
  - `title` (CharField, max length 200)
  - `author` (CharField, max length 100)
  - `publication_year` (IntegerField)

---

## Admin Interface

The `Book` model is registered with the Django admin with the following configurations:

- **list_display:** `title`, `author`, `publication_year`
- **list_filter:** `author`, `publication_year`
- **search_fields:** `title`, `author`

You can access the admin at:

http://127.0.0.1:8000/admin/


> Use a superuser account created via `python manage.py createsuperuser`.

---

## CRUD Operations

All CRUD operations are documented in Markdown files in the `bookshelf` folder:

| Operation | File |
|-----------|------|
| Create    | create.md |
| Retrieve  | retrieve.md |
| Update    | update.md |
| Delete    | delete.md |

Example commands include:

```python
# Create a new book
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Retrieve a book
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Delete the book
book.delete()
