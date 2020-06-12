from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

GENDER = (
    ('female','female'),
    ('male','male')
)

class Userdata(models.Model):
    
    user_first_name = models.CharField(max_length = 50)
    user_last_name = models.CharField(max_length=50)
    user_gender = models.CharField(max_length = 50)
    user_email = models.CharField(max_length = 60)
    user_address = models.CharField(max_length = 100)
    is_user_logged = models.BooleanField()
    user_image = models.CharField(max_length = 500)


@receiver(post_save,sender = settings.AUTH_USER_MODEL)
def auth_token(sender,instance=None,created = False,**kwargs):
    if created:
        Token.objects.create(user=instance)    
