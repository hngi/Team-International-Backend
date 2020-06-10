from django.urls import path, include

from .views import users_view

urlpatterns = [
    path('api/team-international/user/logged', users_view, name='users')
]
