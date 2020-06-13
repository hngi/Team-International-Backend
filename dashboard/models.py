import uuid
from django.db import models


class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50, unique=False)
    last_name = models.CharField(max_length=50, unique=False)
    email = models.CharField(unique=True, max_length=50, null=False)
    phone_number = models.CharField(unique=True, null=False, blank=False, max_length=100)
    age = models.PositiveIntegerField(null=False, blank=False)
    user_logged_in = models.BooleanField(null=True,default=False)
    password = models.CharField(null=False, max_length=255)
    token_exp = models.IntegerField(null=True)
