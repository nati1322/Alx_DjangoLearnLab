from django.urls import path
from . import views
from django.contrib.auth import views as auth_views #import built-in auth views

urlpatterns = [
     path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/new/', views.PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('posts/<int:pk>/comments/new/', views.CommentCreateView.as_view, name='add_comment'),
    path('comments/<int:pk>/update/',views.CommentUpdateView.as_view(), name='comment-update'),
    path('comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
    path('tags/<slug:tag_slug>/', views.PostByTagListView.as_view(), name='post-by-tag'),
    path('search/', views.SearchPostsView.as_view(), name='search-posts'),
]