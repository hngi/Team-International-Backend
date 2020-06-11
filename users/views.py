import json
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getdata(request):
    file = open('user-data.json')
    value = file.read()
    file.close()
    json_data = json.loads(value)
    json_data = [i for i in json_data if i['is_user_logged']]
    return Response({'logged_users':json_data})
