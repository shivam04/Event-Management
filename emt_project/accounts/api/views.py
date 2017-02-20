from .serializers import (
	NormalUsersListSerializer,
    NormalUsersDetailSerializer,
    NormalUserCreateUpdateSerializer,
    UserLoginSerializer,
    UserDetailSerializer,
	)
from django.db.models import Q
from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
    )
from rest_framework.response import Response
from rest_framework.views import APIView

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
from django.contrib.auth.models import User
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
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

class AllUserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

class LoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer
    
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)