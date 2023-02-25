from django.urls import re_path,path
from .views import blog_timeline

urlpatterns = [
    path("timeline/",blog_timeline,name='timeline')
]