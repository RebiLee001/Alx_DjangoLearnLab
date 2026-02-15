from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Blog post URLs (your existing ones)
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/new/', views.PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/', views.ProfileView.as_view(), name='profile'),

# List all posts
    path('', views.PostListView.as_view(), name='post-list'),
    # View a single post
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    # Create a new post
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    # Update an existing post
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    # Delete a post
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

# ----------------------
    # Comment CRUD
    # ----------------------

    # Create comment for a specific post
    path(
        'post/<int:pk>/comments/new/',
        views.CommentCreateView.as_view(),
        name='comment-create'
    ),

    # Update a specific comment
    path(
        'comment/<int:pk>/update/',
        views.CommentUpdateView.as_view(),
        name='comment-update'
    ),

    # Delete a specific comment
    path(
        'comment/<int:pk>/delete/',
        views.CommentDeleteView.as_view(),
        name='comment-delete'
    ),

]


