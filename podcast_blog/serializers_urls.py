from django.urls import path
from podcast_blog import serializers_view


urlpatterns = [
    # view
    path('blogs/', serializers_view.api_detail_blogs_view),
    path('blogs/<int:pk>/', serializers_view.api_detail_blog_view),
    path('comments/', serializers_view.api_detail_comments_view),
    path('comment/<int:pk>/', serializers_view.api_detail_comment_view),
    #edit
    path('blogs/', serializers_view.api_detail_blogs_view),

    #delete
]