from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library  # <-- Library MUST be explicitly imported
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

# Function-based view
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


# Class-based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # <-- REQUIRED
    context_object_name = "library"

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

 class CustomLoginView(LoginView):
    template_name = "relationship_app/login.html"

  class CustomLogoutView(LogoutView):
    template_name = "relationship_app/logout.html"

  # Admin view
@user_passes_test(lambda u: u.userprofile.role == "Admin")
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

# Librarian view
@user_passes_test(lambda u: u.userprofile.role == "Librarian")
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")

# Member view
@user_passes_test(lambda u: u.userprofile.role == "Member")
def member_view(request):
    return render(request, "relationship_app/member_view.html")