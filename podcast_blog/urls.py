from django.urls import re_path,path
from .views import blog_timeline,PodcastBlogCreateView,BlogDeleteView,like_blog,unlike_blog

urlpatterns = [
    path("timeline/",blog_timeline,name='timeline'),
    path('add_blog/<int:pk>/', PodcastBlogCreateView.as_view(), name='create_blog'),
    path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog-delete'),
    path('blog/<int:blog_id>/like/', like_blog, name='like_blog'),
    path('blog/<int:blog_id>/unlike/', unlike_blog, name='unlike_blog'),

]