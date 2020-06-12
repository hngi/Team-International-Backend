from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import json


with open('user-data.json', 'r') as file:
	f = file.read()


class UserList(APIView):
    def get(self, request):
        users = json.loads(f)

        logged_users = []

        for user in users:
        	if user['is_user_logged']:
        		logged_users.append(user)

        return Response(logged_users)
