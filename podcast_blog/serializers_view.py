from rest_framework import generics, permissions
from .models import Podcast_Blog,BlogComment
from .serializers import Podcast_BlogSerializer,BlogCommentSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework import permissions,authentication
from django.contrib.auth.decorators import login_required




# List of data from  all blogs
@api_view(['GET'])
def api_detail_blogs_view(request):
    try:
        users = Podcast_Blog.objects.all()
    except Podcast_Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Podcast_BlogSerializer(users, many=True) # set many=True
        return Response(serializer.data)

# List of data for only one blog set by PK
@api_view(['GET'])
def api_detail_blog_view(request, pk):

    try:
        users = Podcast_Blog.objects.get(pk=pk)
    except Podcast_Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializers = Podcast_BlogSerializer(users)
        return Response(serializers.data)

# List of data from  all comment
@api_view(['GET'])
def api_detail_comments_view(request):
    try:
        users = BlogComment.objects.all()
    except BlogComment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BlogCommentSerializer(users, many=True) # set many=True
        return Response(serializer.data)

# List of data for only one comment set by PK
@api_view(['GET'])
def api_detail_comment_view(request, pk):

    try:
        users = BlogComment.objects.get(pk=pk)
    except BlogComment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializers = BlogCommentSerializer(users)
        return Response(serializers.data)
