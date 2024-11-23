from django.urls import path
from .views import RegisterView, LoginView, UserListView, UserDetailView, UserSearchView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/', UserListView.as_view(), name='users'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='userOne'),
    path('users/search/', UserSearchView.as_view(), name='user-search'),
]
