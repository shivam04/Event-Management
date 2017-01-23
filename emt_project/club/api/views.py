from .serializers import (
	ClubListSerializer,
    ClubCreateUpdateSerializer,
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
class ClubListAPIView(ListAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubListSerializer

class ClubCreateAPIView(CreateAPIView):
    queryset = Club.objects.all()
    #allowed_methods = ('GET','POST')
    serializer_class = ClubCreateUpdateSerializer
    # def perform_create(self,serializer):
    #     serializer.save()

    #allowed_methods = ('get', 'post', 'put', 'delete','patch')