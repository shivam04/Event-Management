from __future__ import unicode_literals
from django.db.models.signals import pre_save

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here.
class City(models.Model):
	city_name = models.CharField(max_length=50)
	total_locality = models.IntegerField(default=0)
	total_venues = models.IntegerField(default=0)
	def __unicode__(self):
		return self.city_name

	def __str__(self):
		return self.city_name

class Locality(models.Model):
	locality_name = models.CharField(max_length=50)
	city_name = models.ForeignKey(City)
	total_venues = models.IntegerField(default=0)
	def __unicode__(self):
		return self.locality_name

	def __str__(self):
		return self.locality_name

class Venues(models.Model):
	venue_name = models.CharField(max_length=50)
	venue_city = models.ForeignKey(City)
	venue_locality = models.ForeignKey(Locality)
	def __unicode__(self):
		return self.venue_name

	def __str__(self):
		return self.venue_name


class Address(models.Model):
	venue = models.ForeignKey(Venues)
	address_line = models.CharField(max_length=150)
	zip_code = models.CharField(max_length=50)
	lon = models.CharField(max_length=50)
	let = models.CharField(max_length=50)


def pre_save_venue_receiver(sender, instance, *args, **kwargs):
	city_qs = City.objects.filter(city_name=instance.venue_city).first()
	city_qs.total_venues = city_qs.total_venues + 1
	city_qs.save()
	loclity_qs = Locality.objects.filter(locality_name=instance.venue_locality).first()
	loclity_qs.total_venues = loclity_qs.total_venues + 1
	loclity_qs.save()
pre_save.connect(pre_save_venue_receiver, sender=Venues)