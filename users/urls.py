from django.urls import path, include

from .views import UserList

urlpatterns = [
    path('api/team-international/user/logged', UserList.as_view(), name='users'),
]
