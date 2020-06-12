from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import json


from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import response, schemas

@api_view()
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='Docs')
    return response.Response(generator.get_schema(request=request))

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
