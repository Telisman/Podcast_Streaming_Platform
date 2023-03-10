from rest_framework import generics
from .models import  Country, PodcastUser, UserInfo
from .serializers import  CountrySerializer, PodcastUserSerializer, UserInfoSerializer





class CountryList(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CountryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer



class PodcastUserList(generics.ListCreateAPIView):
    queryset = PodcastUser.objects.all()
    serializer_class = PodcastUserSerializer

class PodcastUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PodcastUser.objects.all()
    serializer_class = PodcastUserSerializer

class UserInfoList(generics.ListCreateAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

class UserInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer


