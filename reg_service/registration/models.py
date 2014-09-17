from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class UserProfile(models.Model):
	user = models.ForeignKey(User, unique=True)
	created_date = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	role = models.CharField(max_length=255)

	def name(self):
		return self.first_name + " " + self.last_name

