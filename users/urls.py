from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view

from .views import UserList

schema_view = get_swagger_view(title="Docs")

urlpatterns = [
    path('api/team-international/user/logged', UserList.as_view(), name='users'),
    path('docs/', schema_view),
]
