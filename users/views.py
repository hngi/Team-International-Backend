from django.shortcuts import render

from .serializers import UserSerializer


def users_view(request):
	users = UserSerializer

	return render(request, 'users.html', {'users': users})