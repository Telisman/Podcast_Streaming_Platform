from django.urls import path
from .serializers_view import  BlogCommentList, BlogCommentDetail,Podcast_BlogList,Podcast_BlogDetail


urlpatterns = [

    path('blog-comments/', BlogCommentList.as_view(), name='blog-comment-list'),
    path('blog-comments/<int:pk>/', BlogCommentDetail.as_view(), name='blog-comment-detail'),
    path('podcast-blogs/', Podcast_BlogList.as_view(), name='podcast-blog-list'),
    path('podcast-blogs/<int:pk>/', Podcast_BlogDetail.as_view(), name='podcast-blog-detail'),

]