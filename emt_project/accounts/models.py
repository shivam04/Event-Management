from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class NormalUser(models.Model):
	user = models.OneToOneField(User)
	#comapny = models.CharField(max_length=100)
	aadhar_card = models.CharField(default=1234567890,max_length=20)

	def __unicode__(self):
		return self.user.username

	def __str__(self):
		return self.user.username 

	def user_detail(self):
		return User.objects.filter(username=self.user.username)

class CorporateUser(models.Model):
	user = models.OneToOneField(User)
	comapny_name = models.CharField(max_length=100)
	aadhar_card = models.CharField(max_length=20)
	def __unicode__(self):
		return self.user.username

	def __str__(self):
		return self.user.username