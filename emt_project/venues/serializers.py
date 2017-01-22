from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField
    )
from .models import City

class CityListSerializer(ModelSerializer):
	class Meta:
		model = City
		fields = '__all__'