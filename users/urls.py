from django.urls import path
from .views import getdata
urlpatterns = [
    path('logged/',  getdata)
    
]
