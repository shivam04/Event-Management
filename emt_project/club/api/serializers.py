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
club_detail_url = HyperlinkedIdentityField(
        view_name='club-api:club_detail',
        lookup_field='club_slug'
        )
class ClubListSerializer(ModelSerializer):
	#user_name = SerializerMethodField()
	city = SerializerMethodField()
	locality = SerializerMethodField()
	url = club_detail_url
	slug = SerializerMethodField()
	class Meta:
		model = Club
		fields = [
			'club_name',
			'description',
			'city',
			'locality',
			'slug',
			'url',
		]
	def get_slug(self,obj):
		return obj.club_slug
	def get_user_name(self, obj):
		return obj.user.username
	def get_city(self,obj):
		return str(obj.get_city())
	def get_locality(self,obj):
		return str(obj.get_locality())

class ClubDetailSerializer(ModelSerializer):
	user_name = SerializerMethodField()
	city = SerializerMethodField()
	locality = SerializerMethodField()
	entry_type = SerializerMethodField()
	services = SerializerMethodField()
	class Meta:
		model = Club
		fields = [
			'club_name',
			'user_name',
			'city',
			'locality',
			'description',
			'club_slug',
			'entry_type',
			'services',
		]
	def get_user_name(self, obj):
		return obj.user.username
	def get_city(self,obj):
		return str(obj.get_city())
	def get_locality(self,obj):
		return str(obj.get_locality())
	def get_entry_type(self,obj):
		return EntrySerializer(obj.get_entry_rates(),many=True).data
	def get_services(self,obj):
		return ServiceSerializer(obj.get_service(),many=True).data

class EntrySerializer(ModelSerializer):
	class Meta:
		model = Entry_rate
		fields = '__all__'
class ServiceSerializer(ModelSerializer):
	class Meta:
		model = Service
		fields = '__all__'
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

