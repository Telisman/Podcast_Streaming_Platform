from django.urls import re_path,path
from .views import login_and_register,logout_view,PodcastDashboard,FAQ,Navbar_footer_menu


urlpatterns = [
    path('navbar_footer_menu/', Navbar_footer_menu, name='navbar_footer_menu'),
    path('login_and_register/', login_and_register, name='login_and_register'),
    path('podcast_dashboard/', PodcastDashboard, name='podcast_dashboard'),
    path('logout/', logout_view, name='logout'),
    path('FAQ/', FAQ, name='faq'),
    # path('ViewPodcast/', ViewPodcast.as_view(), name="ViewPodcast"),
    # path('confirm_user_request/<int:user_id>/', confirm_user_request, name='confirm_user_request'),
]