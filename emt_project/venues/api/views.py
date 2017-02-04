from .serializers import (
	CityListSerializer,
	CityDetailSerializer,
	LocalityListSerializer,
	LocalityDetailSerializer,
	VenueCreateUpdateSerializer,
	)
from django.db.models import Q
from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
    )

from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView, 
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
    )
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

    )
from venues.models import (
	City,
	Locality,
	Venues,
	Address,
	)

class CityDetailAPIView(RetrieveAPIView):
	queryset = City.objects.all()
	serializer_class = CityDetailSerializer
	lookup_field = 'city_slug'

class CityLocalityListAPIView(ListAPIView):
	queryset = City.objects.all()
	serializer_class = CityDetailSerializer

class CityListAPIView(ListAPIView):
	#queryset = City.objects.all()
	serializer_class = CityListSerializer
	search_field = ['city_name']
	#permission_classes = ['IsSuperUser']
	def get_queryset(self, *args, **kwargs):
		queryset_list = City.objects.all() #super(PostListAPIView, self).get_queryset(*args, **kwargs)
		query = self.request.GET.get("city")
		if query:
			queryset_list = queryset_list.filter(Q(city_name__icontains=query)
					).distinct()
		return queryset_list

class LocalityDetailAPIView(RetrieveAPIView):
	queryset = Locality.objects.all()
	serializer_class = LocalityDetailSerializer
	lookup_field = 'locality_slug'



class LocalityListAPIView(ListAPIView):
	#queryset = City.objects.all()
	serializer_class = LocalityListSerializer
	search_field = ['locality_name']
	def get_queryset(self, *args, **kwargs):
		queryset_list = Locality.objects.all() #super(PostListAPIView, self).get_queryset(*args, **kwargs)
		query = self.request.GET.get("locality")
		print query
		if query:
			queryset_list = queryset_list.filter(Q(locality_name__icontains=query)
					).distinct()
		return queryset_list
class VenueCreateAPIView(CreateAPIView):
	queryset = Venues.objects.all()
	serializer_class = VenueCreateUpdateSerializer

class VenueUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Venues.objects.all()
	serializer_class = VenueCreateUpdateSerializer
	lookup_field = 'id'
	#permission_classes = ['IsAuthenticatedOrReadOnly']
	def perform_update(self, serializer):
		serializer.save()


	# def perform_update(self, serializer):
	# 	serializer.save()

# class VenueDetailAPIView(RetrieveAPIView):
# 	queryset = Venues.objects.all()
# 	serializer_class = VenueDetailSerializer
# 	lookup_field = 'locality_slug'



# class LocalityListAPIView(ListAPIView):
# 	#queryset = City.objects.all()
# 	serializer_class = LocalityListSerializer
# 	search_field = ['locality_name']
# 	def get_queryset(self, *args, **kwargs):
# 		queryset_list = Locality.objects.all() #super(PostListAPIView, self).get_queryset(*args, **kwargs)
# 		query = self.request.GET.get("locality")
# 		print query
# 		if query:
# 			queryset_list = queryset_list.filter(Q(locality_name__icontains=query)
# 					).distinct()
# 		return queryset_list