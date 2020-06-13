import datetime

import jwt
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from TeamInternationalBackend import settings
from .models import UserProfile
from dashboard.serializers import UserSerializer
import time


@api_view(['GET'])
def user_details(request):
    # Query params=>account id,token
    if request.method == 'GET':
        accountID = request.query_params.get('account_id')
        token = request.query_params.get('token')
        vaildate_token = jwt.decode(token, settings.SECRET_KEY, algorithm='HS256')
        if vaildate_token['id'] == accountID:
            if time.time() < vaildate_token['exp']:
                snippets = UserProfile.objects.filter(user_logged_in=True)
                serializer = UserSerializer(snippets, many=True)
                return JsonResponse(serializer.data, safe=False)
            else:
                return JsonResponse({
                    "message": "Token got expired .Login again to get a new token",
                    status: status.HTTP_401_UNAUTHORIZED
                }, safe=False)
        else:
            return JsonResponse({
                "message": "Invalid token.",
                status: status.HTTP_400_BAD_REQUEST
            }, safe=False)


@api_view(['POST'])
def user_creation_details(request):
    if request.method == 'POST':
        request.data.user_logged_in = False
        print(request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['POST'])
def get_auth_token(request):
    if request.method == 'POST':
        email = request.data['email']
        password = request.data['password']
        user = UserProfile.objects.get(email=email, password=password)
        if user:
            try:
                userData = UserSerializer(user, many=False).data
                userData['exp'] = datetime.datetime.utcnow() + datetime.timedelta(seconds=86400)
                token = jwt.encode(userData, settings.SECRET_KEY, algorithm='HS256')
                user.user_logged_in = True
                user.token_exp = userData['exp']
                user.save()
                data = {
                    'message': 'Retreived token successfully',
                    'data': {
                        'client_id': userData['id'],
                        'auth_token': token.decode("utf-8")
                    },
                    "status": status.HTTP_200_OK
                }
                return JsonResponse(data, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                res = {'error': e, status: status.HTTP_403_FORBIDDEN}
                return JsonResponse(res, status=status.HTTP_403_FORBIDDEN)
        else:
            res = {
                'error': 'invalid email id or password', status: status.HTTP_400_BAD_REQUEST}
            return JsonResponse(res, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def logout(request):
    if request.method == 'PUT':
        accountID = request.data['account_id']
        user = UserProfile.objects.get(id=accountID)
        if user:
            try:
                userData = UserSerializer(user, many=False).data
                if userData['user_logged_in']:
                    user.user_logged_in = False
                    user.token_exp = None
                    user.save()
                    data = {
                        'message': 'Logged out successfully',
                        "status": status.HTTP_200_OK
                    }
                    return JsonResponse(data, status=status.HTTP_200_OK)
                else:
                    data = {
                        'message': 'Login inorder to log out ',
                        "status": status.HTTP_200_OK
                    }
                    return JsonResponse(data, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                res = {'error': e, status: status.HTTP_403_FORBIDDEN}
                return JsonResponse(res, status=status.HTTP_403_FORBIDDEN)
        else:
            res = {
                'error': 'There is client with this id', status: status.HTTP_400_BAD_REQUEST}
            return JsonResponse(res, status=status.HTTP_400_BAD_REQUEST)
