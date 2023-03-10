from rest_framework import serializers
from .models import PodcastUser,UserInfo,Country

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