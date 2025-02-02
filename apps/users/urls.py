from django.urls import path
from .views import UserListView
from .views import UserProfileView


urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
]
