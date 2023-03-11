from rest_framework import serializers
from .models import PodcastUser,UserInfo,Country
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'
class PodcastUserSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)

    class Meta:
        model = PodcastUser
        fields = ['user_id', 'first_name', 'last_name', 'username', 'phone_number', 'date_of_birth', 'date_of_join',
                  'address', 'image', 'city_name', 'country', 'postal_code', 'email', 'followers']


class UserInfoSerializer(serializers.ModelSerializer):
    user = PodcastUserSerializer(read_only=True)

    class Meta:
        model = UserInfo
        fields = ['user', 'bio', 'language', 'education', 'skills']


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = PodcastUser
        fields = ('email', 'password', 'first_name', 'last_name', 'username', 'country')

    def create(self, validated_data):
        user = PodcastUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            country=validated_data['country']
        )
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(email=data['email'], password=data['password'])
        if user and user.is_active:
            data['user'] = user
            return data
        raise serializers.ValidationError('Incorrect email or password.')