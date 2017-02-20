from rest_framework.serializers import (
	CharField,
	EmailField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
    )
from django.contrib.auth import get_user_model
from django.db.models import Q

from django.contrib.auth.models import User
from accounts.models import NormalUser,CorporateUser
user_url = HyperlinkedIdentityField(
	view_name='users-api:user_detail',
    lookup_field='id',
	) 
from django.utils.crypto import get_random_string
from django.core import serializers
User = get_user_model()
class NormalUsersListSerializer(ModelSerializer):
	user_name = SerializerMethodField()
	url = user_url
	class Meta:
	    model = NormalUser
	    fields = [
	    	'user_name',
	    	'user',
	    	'url',
	        'aadhar_card',

	    ]
	def get_user_name(self,obj):
		user = obj.user.username
		return user
class UserDetailSerializer(ModelSerializer):
	#password = serializers.CharField(write_only=True)

	def create(self, validated_data):

		user = User.objects.create(
		username=validated_data['username'],
		first_name=validated_data['first_name'],
		last_name=validated_data['last_name'],
		email = validated_data['email']
		)
		user.set_password(validated_data['password'])
		user.save()

		return user
	class Meta:
		model = User
		fields = ('id','username','password', 'first_name', 'last_name', 'email',)
		write_only_fields = ('password',)
	# def create(self, validated_data):
	# 	# call set_password on user object. Without this
	# 	# the password will be stored in plain text.
	# 	user = super(UserDetailSerializer, self).create(validated_data)
	# 	user.set_password(validated_data['password'])
	# 	return user
class NormalUsersDetailSerializer(ModelSerializer):
	#user_name = SerializerMethodField()
	user_detail = SerializerMethodField()
	class Meta:
	    model = NormalUser
	    fields = [
	    	'user',
	    	'user_detail',
	        'aadhar_card',
	    ]
	def get_user_detail(self,obj):
		# u =  obj.user
		# context = {'user_name':u.username,
		# 	'first_name':u.first_name,
		# 	'last_name':u.last_name,
		# 	'email':u.email}
		# user_detail = serializers.serialize("json",u)
		# return user_detail
		return UserDetailSerializer(obj.user_detail(),many=True).data
class NormalUserCreateUpdateSerializer(ModelSerializer):
	user_detail = SerializerMethodField()
	class Meta:
	    model = NormalUser
	    fields = [
	        'user',
	        'aadhar_card',
	        'user_detail',
	    ]
	def get_user_detail(self,obj):
		return UserDetailSerializer(obj.user_detail(),many=True).data
class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField(required=False, allow_blank=True)
    #email = EmailField(label='Email Address', required=False, allow_blank=True)
    class Meta:
        model = User
        fields = [
            'username',
            #'email',
            'password',
            'token',
            
        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                            }
    def validate(self, data):
        #email = data.get("email",None)
        username = data.get("username",None)
        password = data.get("password",None)
        #user_qs = User.objects.filter(email=email)
        if not username:
            raise ValidationError("A usrname  is required to login.")
        user = User.objects.filter(
                Q(username =username)
            ).distinct()
        #user = user.exclude(email__isnull=True).exclude(email__iexact='')
        if user.exists() and user.count()==1:
            user_obj = user.first()
        else:
            raise ValidationError("This Username/email is not valid.")

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect Credentials Please Try again.")
        data['token'] = get_random_string(length=15)
        return data