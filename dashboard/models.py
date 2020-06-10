from django.db import models

# Create your models here.
GENDER = (
    ('female', 'female'),
    ('male', 'male')
)


class UserData(models.Model):
    user_first_name = models.CharField(max_length=60)
    user_last_name = models.CharField(max_length=60)
    user_gender = models.CharField(max_length=6, choices=GENDER)
    user_email = models.CharField(max_length=60)
    user_address = models.CharField(max_length=200)
    is_user_logged = models.BooleanField()
    user_image = models.CharField(max_length=1000)

    def __str__(self):
        """A string representation of the model."""
        return self.user_first_name+' '+self.user_last_name
