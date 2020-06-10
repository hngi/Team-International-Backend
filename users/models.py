from django.db import models

class User(models.Model):
	user_id = models.CharField(max_length=50)
	user_first_name = models.CharField(max_length=50)
	user_last_name = models.CharField(max_length=50)
	user_gender = models.CharField(max_length=50)
	user_address = models.CharField(max_length=50)
	user_email = models.CharField(max_length=50)
	user_image = models.CharField(max_length=50)
	is_user_logged = models.BooleanField()

	def __str__(self):
		return f"{self.user_first_name} {self.user_last_name}"
