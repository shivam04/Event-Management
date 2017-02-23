from __future__ import unicode_literals
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
class Status(models.Model):
	status_name = models.CharField(max_length=50)

class Booking(models.Model):
	fromdate = models.DateTimeField(auto_now=False , auto_now_add=False)
	status_id = models.ForeignKey(Status)
	todate = models.DateTimeField(auto_now=False , auto_now_add=False)
	total = models.DecimalField(max_digits=8,decimal_places=2 )
	date_time = models.DateTimeField(auto_now=True,auto_now_add=False)
	user = models.ForeignKey(settings.AUTH_USER_MODEL)



class OrderVenue(models.Model):
	venue_type = models.ForeignKey(ContentType,on_delete=models.CASCADE,default=None)
	object_id = models.PositiveIntegerField(default=0)
	venue_object = GenericForeignKey('venue_type', 'object_id')
	booking_id = models.ForeignKey(Booking)

class Payment_Method(models.Model):
	payment_method = models.CharField(max_length=50)

class Payment(models.Model):
	invoice_number = models.CharField(max_length=50)
	payment_method = models.ForeignKey(Payment_Method)
	booking_id = models.ForeignKey(Booking)
	amount = models.DecimalField(max_digits=8,decimal_places=2)
	date_time = models.DateTimeField(auto_now=True,auto_now_add=False)
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
