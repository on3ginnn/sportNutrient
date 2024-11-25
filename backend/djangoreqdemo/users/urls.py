from django.urls import path
from .views import RegisterView, LoginView, UserListView, UserDetailView, UserSearchView, UserProfileView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/', UserListView.as_view(), name='users'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='userOne'),
    path('users/search/', UserSearchView.as_view(), name='user-search'),
]
