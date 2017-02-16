from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
    )
from club.models import (
	Club,
	Entry_rate,
	Service,
	)
from venues.api.serializers import VenuesListSerializer
import json

def filter_by_city_serializer(city=None,locality=None):
	class ClubListCitySerializer(ModelSerializer):
		user_name = SerializerMethodField()
		city = SerializerMethodField()
		locality = SerializerMethodField()
		class Meta:
			model = Club
			fields = [
				'club_name',
				'user_name',
			]
		def get_user_name(self, obj):
			return obj.user.username
		def get_city(self,obj):
			return str(obj.get_city())
		def get_locality(self,obj):
			return str(obj.get_locality())
	return ClubListCitySerializer
class ClubCreateUpdateSerializer(ModelSerializer):
	venue = SerializerMethodField()
	class Meta:
	    model = Club
	    fields = [
	        'club_name',
	        'user',
	        'venue',
	    ]
	def get_venue(self,obj):
		return VenuesListSerializer(obj.create_venue()).data
class ClubListSerializer(ModelSerializer):
	user_name = SerializerMethodField()
	city = SerializerMethodField()
	locality = SerializerMethodField()
	class Meta:
		model = Club
		fields = [
			'club_name',
			'user_name',
			'city',
			'locality',
		]
	def get_user_name(self, obj):
		return obj.user.username
	def get_city(self,obj):
		return str(obj.get_city())
	def get_locality(self,obj):
		return str(obj.get_locality())

# class VenuesListSerializer(ModelSerializer):
# 	address = SerializerMethodField()
# 	class Meta:
# 		model = Venues
# 		fields = [
# 			'venue_name',
# 			'address',
# 		]
# 	def get_address(self,obj):
# 		return AddressListSerializer(obj.children(),many=True).data

# locality_detail_url = HyperlinkedIdentityField(
#         view_name='venue-api:locality_detail',
#         lookup_field='locality_slug'
#         )
# class LocalityListSerializer(ModelSerializer):
# 	url = locality_detail_url
# 	class Meta:
# 		model = Locality
# 		fields = [
# 			'locality_name',
# 			'url',
# 			'total_venues',
# 		]

# class LocalityDetailSerializer(ModelSerializer):
# 	venue = SerializerMethodField()
# 	city = SerializerMethodField()
# 	class Meta:
# 		model = Locality
# 		fields = [
# 			'locality_name',
# 			'venue',
# 			'total_venues',
# 			'city',
# 		]
# 	def get_venue(self,obj):
# 		return VenuesListSerializer(obj.children(),many=True).data
# 	def get_city(self,obj):
# 		print obj.city_name
# 		return str(obj.city_name)
		 

# city_detail_url = HyperlinkedIdentityField(
#         view_name='venue-api:detail',
#         lookup_field='city_slug'
#         )

# class CityDetailSerializer(ModelSerializer):
# 	locality = SerializerMethodField()
# 	class Meta:
# 		model = City
# 		fields = [
# 			'city_name',
# 			'locality'
# 		]
# 	def get_locality(self,obj):
# 			return LocalityDetailSerializer(obj.children(),many=True).data

# class CityListSerializer(ModelSerializer):
# 	url = city_detail_url
# 	class Meta:
# 		model = City
# 		fields = [
# 			'city_name',
# 			'url',
# 			'total_venues',
# 		]