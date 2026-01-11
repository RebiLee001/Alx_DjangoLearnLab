from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # columns to show
    list_filter = ('publication_year', 'author')            # filter sidebar
    search_fields = ('title', 'author')                     # search box

# Register model with custom admin
admin.site.register(Book, BookAdmin)


# Register your models here.
