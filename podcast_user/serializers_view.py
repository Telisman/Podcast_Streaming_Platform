from rest_framework import generics
from .models import  Country, PodcastUser, UserInfo
from .serializers import  CountrySerializer, PodcastUserSerializer, UserInfoSerializer,UserLoginSerializer,UserRegistrationSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework import permissions,authentication
from django.contrib.auth.decorators import login_required



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


# API registration view
class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# API login view
class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# List of data for all users
@api_view(['GET', ])
def api_detail_user_view(request, pk):

    try:
        users = PodcastUser.objects.get(pk=pk)
    except PodcastUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializers = PodcastUserSerializer(users)
        return Response(serializers.data)
# View user data for only one user, set by pk
@api_view(['GET'])
def api_detail_users_view(request):
    try:
        users = PodcastUser.objects.all()
    except PodcastUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PodcastUserSerializer(users, many=True) # set many=True
        return Response(serializer.data)

# Edit user info, only if user is login with token using PUT method
@api_view(['PUT'])
@login_required
def api_update_user_view(request, pk):
    try:
        user = PodcastUser.objects.get(pk=pk)
    except PodcastUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PodcastUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)