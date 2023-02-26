from django.urls import re_path,path
from .views import blog_timeline,add_blog

urlpatterns = [
    path("timeline/",blog_timeline,name='timeline'),
    path("profile_page/add_new_blog/",add_blog,name='new_blog')
]