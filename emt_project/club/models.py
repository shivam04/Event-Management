from __future__ import unicode_literals
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from venues.models import Venues,City,Locality
from django.contrib.auth.models import User
from django.conf import settings
from venues.models import Venues

class Club(models.Model):
	club_name = models.CharField(max_length=50)
	club_slug = models.SlugField(unique=True,default=None)
	user = models.ForeignKey(settings.AUTH_USER_MODEL)

	#obj = ClubManager()
	def __unicode__(self):
		return self.club_name			

	def __str__(self):
		return self.club_name

	def create_venue(self):
		print self.id
		content_type = ContentType.objects.get_for_model(self.__class__)
		city = City.objects.all().first()
		locality = Locality.objects.all().first()
		b = Venues(venue_name=self.club_name,content_type=content_type,object_id=self.id,venue_city=city,venue_locality=locality)
		b.save()
		return b
	def get_city(self):
		#print self.id
		city_filter = Venues.objects.filter(object_id=self.id)
		city_filter = city_filter.first()
		return city_filter.venue_city
	def get_locality(self):
		locality_filter = Venues.objects.filter(object_id=self.id)
		locality_filter = locality_filter.first()
		return locality_filter.venue_locality
	# def children(self):
	# 	return Locality.objects.filter(service_name=self.id)

class Entry_rate(models.Model):
	entry_type = models.CharField(max_length=20)
	club_name = models.ForeignKey(Club)
	price = models.IntegerField(default=0)
	# locality_slug = models.SlugField(unique=True,default=None)
	def __unicode__(self):
		return self.entry_type

	def __str__(self):
		return self.entry_type

	# def children(self):
	# 	return Venues.objects.filter(venue_locality=self.id,venue_city=self.city_name)

	

class Service(models.Model):
	service_name = models.CharField(max_length=50)
	club_name = models.ForeignKey(Club)
	
	def __unicode__(self):
		return self.service_name

	def __str__(self):
		return self.service_name

	# def children(self):
	# 	return Address.objects.filter(venue=self.id)

# class Address(models.Model):
# 	venue = models.ForeignKey(Venues)
# 	address_line = models.CharField(max_length=150)
# 	zip_code = models.CharField(max_length=50)
# 	lon = models.CharField(max_length=50)
# 	let = models.CharField(max_length=50)

def create_slug(instance ,new_slug=None):
	slug = slugify(instance.club_name)
	if new_slug is not None:
		slug = new_slug
	qs = Club.objects.filter(club_slug=slug).order_by("-id")
	exists = qs.exists()
	if exists:
		new_slug = slug+"-"+str(qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug
# def pre_save_venue_receiver(sender, instance, *args, **kwargs):
# 	city_qs = City.objects.filter(city_name=instance.venue_city).first()
# 	city_qs.total_venues = city_qs.total_venues + 1
# 	city_qs.save()
# 	loclity_qs = Locality.objects.filter(locality_name=instance.venue_locality).first()
# 	loclity_qs.total_venues = loclity_qs.total_venues + 1
# 	loclity_qs.save()

# def pre_save_city_slug(sender, instance, *args, **kwargs):
# 	if not instance.city_slug:
# 		instance.city_slug = instance.city.lower()
def pre_save_club_slug(sender, instance, *args, **kwargs):
	if not instance.club_slug:
		instance.club_slug = create_slug(instance)
#pre_save.connect(pre_save_venue_receiver, sender=Venues)

pre_save.connect(pre_save_club_slug, sender=Club)

# pre_save.connect(pre_save_locality_slug, sender=Locality)