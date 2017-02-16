from .serializers import (
	ClubListSerializer,
    ClubCreateUpdateSerializer,
    filter_by_city_serializer,
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
from club.models import (
    Club,
    Entry_rate,
    Service,
    )
class ClubListCityAPIView(ListAPIView):
    queryset = Club.objects.all()
    # def get_serializer_class(self):
    #     city = self.request.GET.get("city")
    #     locality = self.request.GET.get("locality")
    #     #parent_id = self.request.GET.get("parent_id", None)
    #     return filter_by_city_serializer(
    #             city=city,
    #             locality=locality,
    #             )
class ClubListAPIView(ListAPIView):
    #queryset = Club.objects.all()
    serializer_class = ClubListSerializer
    def get_queryset(self, *args, **kwargs):
        c_query = self.request.GET.get("city")
        l_query = self.request.GET.get("locality")
        queryset_list = Club.objects.all() #super(PostListAPIView, self).get_queryset(*args, **kwargs)
        
        if c_query and l_query:
            c_query = str(c_query).strip()
            l_query = str(l_query).strip()
            queryset = []
            for query in queryset_list:
                city =  query.get_city()
                city = str(city).strip()
                locality = str(query.get_locality()).strip()
                if city == c_query and locality == l_query:
                    queryset.append(query)
                #print query
            queryset_list = queryset
        return queryset_list

class ClubCreateAPIView(CreateAPIView):
    queryset = Club.objects.all()
    #allowed_methods = ('GET','POST')
    #permission_classes = ['IsAuthenticatedOrReadOnly']
    serializer_class = ClubCreateUpdateSerializer
    # def perform_create(self,serializer):
    #     serializer.save()

    #allowed_methods = ('get', 'post', 'put', 'delete','patch')