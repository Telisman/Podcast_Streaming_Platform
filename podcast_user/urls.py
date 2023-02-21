from django.urls import re_path,path
from .views import login_and_register,logout_view,PodcastDashboard,Navbar_footer_menu,profile_page,users_list


urlpatterns = [
    path('navbar_footer_menu/', Navbar_footer_menu, name='navbar_footer_menu'),
    path('login_and_register/', login_and_register, name='login_and_register'),
    path('podcast_dashboard/', PodcastDashboard, name='podcast_dashboard'),
    path('logout/', logout_view, name='logout'),
    path('profile_page/', profile_page, name='profile_page'),
    path('users_list/', users_list, name='users_list'),
    # path('ViewPodcast/', ViewPodcast.as_view(), name="ViewPodcast"),
    # path('confirm_user_request/<int:user_id>/', confirm_user_request, name='confirm_user_request'),
]