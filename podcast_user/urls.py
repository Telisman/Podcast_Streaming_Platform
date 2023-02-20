from django.urls import re_path,path
from .views import login_and_register,logout_view,test


urlpatterns = [
    re_path(r'^login_and_register/', login_and_register, name='login_and_register'),
    re_path(r'^test/', test, name='test'),
    # re_path(r'^podcast_dashboard/', PodcastDashboard, name='podcast_dashboard'),
    re_path(r'^logout/', logout_view, name='logout'),
    # path('confirm_user_request/<int:user_id>/', confirm_user_request, name='confirm_user_request'),
]