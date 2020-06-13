from rest_framework import serializers

from .models import UserProfile


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        exclude = ('token_exp',)
        extra_kwargs = {'password': {'write_only': True}}




