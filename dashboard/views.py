import json

from rest_framework.response import Response
from rest_framework.views import APIView


class UserDataView(APIView):
    def get(self, request):
        f = open('user-data.json')
        json_string = f.read()
        f.close()
        data = json.loads(json_string)
        data = [x for x in data if x['is_user_logged']]
        return Response({"logged_in_users": data})
