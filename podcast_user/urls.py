from django.urls import re_path,path,include
from .views import login_and_register,logout_view,PodcastDashboard,Navbar_footer_menu,profile_page,users_list,edit_user_info,follow_user,unfollow_user,User_Detail_View
from podcast_blog.views import like_blog,unlike_blog


urlpatterns = [
    path('navbar_footer_menu/', Navbar_footer_menu, name='navbar_footer_menu'),
    path('login_and_register/', login_and_register, name='login_and_register'),
    path('podcast_dashboard/', PodcastDashboard, name='podcast_dashboard'),
    path('logout/', logout_view, name='logout'),
    path('profile_page/', profile_page, name='profile_page'),
    path('users_list/', users_list  , name='users_list'),
    path('edit_user_info/', edit_user_info, name='edit_user_info'),
    # path('user/<int:user_id>/', user_detail, name='user_detail'),
    path('user/<int:pk>/', User_Detail_View.as_view(), name='user_detail'),
    path('user/<int:pk>/follow/', follow_user, name='follow_user'),
    path('user/<int:pk>/unfollow/', unfollow_user, name='unfollow_user'),
    path('user/<int:blog_id>/like/', like_blog, name='like_blog'),
    path('user/<int:blog_id>/unlike/', unlike_blog, name='unlike_blog'),
    # path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
    # path('ViewPodcast/', ViewPodcast.as_view(), name="ViewPodcast"),
    # path('confirm_user_request/<int:user_id>/', confirm_user_request, name='confirm_user_request'),
]