from django.db import models

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