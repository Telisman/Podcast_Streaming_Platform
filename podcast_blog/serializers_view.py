from rest_framework import generics, permissions
from .models import Podcast_Blog,BlogComment
from .serializers import Podcast_BlogSerializer,BlogCommentSerializer

class Podcast_BlogList(generics.ListCreateAPIView):
    queryset = Podcast_Blog.objects.all()
    serializer_class = Podcast_BlogSerializer

class Podcast_BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Podcast_Blog.objects.all()
    serializer_class = Podcast_BlogSerializer


class BlogCommentList(generics.ListCreateAPIView):
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentSerializer

class BlogCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentSerializer