from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
    )
from venues.models import (
	City,
	Locality,
	Venues,
	Address,
	)
from django.core.urlresolvers import reverse
import socket
from django.contrib.contenttypes.models import ContentType
class AddressListSerializer(ModelSerializer):
	class Meta:
		model = Address
		fields = [
			'address_line',
			'zip_code',
			'lon',
			'let',
		]

class VenueCreateUpdateSerializer(ModelSerializer):
	#address = SerializerMethodField()
	class Meta:
	    model = Venues
	    fields = [
	        'venue_name',
	        'content_type',
	        'venue_city',
	        'venue_locality',
	        'object_id',
	        #'address',
	    ]
	#def get_address(self,obj):
		#return AddressListSerializer(obj.children(),many=True).data
# venue_update_url = HyperlinkedIdentityField(
#         view_name='venue-api:update',
#         lookup_field='id'
#         )
class VenuesListSerializer(ModelSerializer):
	update = SerializerMethodField()
	address = SerializerMethodField()
	class Meta:
		model = Venues
		fields = [
			'venue_name',
			'address',
			'update',
		]
	def get_address(self,obj):
		return AddressListSerializer(obj.children(),many=True).data
	def get_update(self,obj):
		return reverse("venue-api:update",kwargs={"id":obj.id})
locality_detail_url = HyperlinkedIdentityField(
        view_name='venue-api:locality_detail',
        lookup_field='locality_slug'
        )
class LocalityListSerializer(ModelSerializer):
	url = locality_detail_url
	class Meta:
		model = Locality
		fields = [
			'locality_name',
			'url',
			'total_venues',
		]

class LocalityDetailSerializer(ModelSerializer):
	venue = SerializerMethodField()
	city = SerializerMethodField()
	class Meta:
		model = Locality
		fields = [
			'locality_name',
			'id',
			'venue',
			'total_venues',
			'city',
			'locality_slug',

		]
	def get_venue(self,obj):
		return VenuesListSerializer(obj.children(),many=True).data
	def get_city(self,obj):
		#print obj.city_name
		return str(obj.city_name)
		 

city_detail_url = HyperlinkedIdentityField(
        view_name='venue-api:detail',
        lookup_field='city_slug'
        )

class CityDetailSerializer(ModelSerializer):
	locality = SerializerMethodField()
	class Meta:
		model = City
		fields = [
			'city_name',
			'locality',

		]
	def get_locality(self,obj):
			return LocalityDetailSerializer(obj.children(),many=True).data

class CityListSerializer(ModelSerializer):
	url = city_detail_url
	class Meta:
		model = City
		fields = '__all__'