from .serializers import (
	NormalUsersListSerializer,
    NormalUsersDetailSerializer,
    NormalUserCreateUpdateSerializer,
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
from accounts.models import (
    NormalUser,
    CorporateUser,
    )

class NormalListAPIView(ListAPIView):
    queryset = NormalUser.objects.all()
    serializer_class = NormalUsersListSerializer
class NormalDetailAPIView(RetrieveAPIView):
    queryset = NormalUser.objects.all()
    serializer_class = NormalUsersDetailSerializer
    lookup_field = 'id'

class NormalUserCreateAPIView(CreateAPIView):
    queryset = NormalUser.objects.all()
    serializer_class = NormalUserCreateUpdateSerializer