from django.urls import path
from .serializers_view  import CountryList,CountryDetail,PodcastUserList,PodcastUserDetail,UserInfoList,UserInfoDetail


urlpatterns = [
    path('countries/', CountryList.as_view(), name='country-list'),
    path('countries/<int:pk>/', CountryDetail.as_view(), name='country-detail'),
    path('podcast-users/', PodcastUserList.as_view(), name='podcast-user-list'),
    path('podcast-users/<int:pk>/', PodcastUserDetail.as_view(), name='podcast-user-detail'),
    path('user-info/', UserInfoList.as_view(), name='user-info-list'),
    path('user-info/<int:pk>/', UserInfoDetail.as_view(), name='user-info-detail'),
]