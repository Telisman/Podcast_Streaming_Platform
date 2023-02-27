from django.urls import re_path,path
from .views import blog_timeline,PodcastBlogCreateView

urlpatterns = [
    path("timeline/",blog_timeline,name='timeline'),
    path('add_blog/<int:pk>/', PodcastBlogCreateView.as_view(), name='create_blog'),
]