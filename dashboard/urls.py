from django.urls import include, path

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
from dashboard.views import UserDataView

urlpatterns = [
    path('users/logged', UserDataView.as_view()),
]