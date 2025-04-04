from django.urls import path
from .views import UserRegistrationView,UserLoginView, FollowUserView, UnfollowUserView, UserListView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow_user'),
    path('users/', UserListView.as_view(), name='user_list'),
]