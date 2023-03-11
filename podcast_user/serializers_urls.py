from django.urls import path
from .serializers_view  import CountryList,CountryDetail,PodcastUserList,PodcastUserDetail,UserInfoList,UserInfoDetail,UserRegistrationView, UserLoginView
from rest_framework.authtoken.views import obtain_auth_token
from podcast_user import serializers_view
urlpatterns = [
    path('countries/', CountryList.as_view(), name='country-list'),
    path('countries/<int:pk>/', CountryDetail.as_view(), name='country-detail'),
    path('podcast-users/', PodcastUserList.as_view(), name='podcast-user-list'),
    path('podcast-users/<int:pk>/', PodcastUserDetail.as_view(), name='podcast-user-detail'),
    path('user-info/', UserInfoList.as_view(), name='user-info-list'),
    path('user-info/<int:pk>/', UserInfoDetail.as_view(), name='user-info-detail'),
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
    path('users/', serializers_view.api_detail_users_view),
    path('user/<int:pk>/', serializers_view.api_detail_user_view),
    path('user/edit/<int:pk>/', serializers_view.api_update_user_view),
    path('user/delete/<int:pk>/', serializers_view.api_delete_user),
]