from django.urls import path
from .views import getdata
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('logged/',  getdata),
    path('login/',ObtainAuthToken,name ="login")
    
]
