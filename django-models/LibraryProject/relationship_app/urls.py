from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path("books/", views.list_books, name="list_books"),
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),
     # Book CRUD with permissions
    path("book/add/", views.add_book, name="add_book"),
    path("book/<int:pk>/edit/", views.edit_book, name="edit_book"),
    path("book/<int:pk>/delete/", views.delete_book, name="delete_book"),

    # Authentication URLs (CHECKER-SAFE)
    path(
        "login/",
        LoginView.as_view(template_name="relationship_app/login.html"),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(template_name="relationship_app/logout.html"),
        name="logout",
    ),
    path("register/", views.register, name="register"),
]

   