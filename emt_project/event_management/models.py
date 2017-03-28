from __future__ import unicode_literals
from django.utils.text import slugify
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class Emt_c(models.Model):
	comp_name = models.CharField(max_length=50)
	comp_slug = models.SlugField(unique=True,default=None)
	description = models.TextField()
	user = models.ForeignKey(settings.AUTH_USER_MODEL)

class Category(models.Model):
	category_name = models.CharField(max_length=50)
	category_slug = models.SlugField(unique=True,default=None)
class Services(models.Model):
	service_name = models.CharField(max_length=50)
	service_slug = models.SlugField(unique=True,default=None)
class Package(models.Model):
	package_type = models.CharField(max_length=10)
	package_cost = models.CharField(max_length=20)
	package_services = models.CharField(max_length=100)
	package_category = models.ForeignKey(Category)
	package_emt = models.ForeignKey(Emt_c)