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
        blogs = Podcast_Blog.objects.all()
    except Podcast_Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Podcast_BlogSerializer(blogs, many=True) # set many=True
        return Response(serializer.data)

# List of data for only one blog set by PK
@api_view(['GET'])
def api_detail_blog_view(request, pk):

    try:
        blog = Podcast_Blog.objects.get(pk=pk)
    except Podcast_Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializers = Podcast_BlogSerializer(blog)
        return Response(serializers.data)

# List of data from  all comment
@api_view(['GET'])
def api_detail_comments_view(request):
    try:
        comments = BlogComment.objects.all()
    except BlogComment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BlogCommentSerializer(comments, many=True) # set many=True
        return Response(serializer.data)

# List of data for only one comment set by PK
@api_view(['GET'])
def api_detail_comment_view(request, pk):

    try:
        comment = BlogComment.objects.get(pk=pk)
    except BlogComment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializers = BlogCommentSerializer(comment)
        return Response(serializers.data)


# edit blog
@api_view(['PUT'])
@login_required
def api_update_blog_view(request, pk):
    try:
        blog = Podcast_Blog.objects.get(pk=pk)
    except Podcast_Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = Podcast_BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# edit comment
@api_view(['PUT'])
@login_required
def api_update_comment_view(request, pk):
    try:
        comment = BlogComment.objects.get(pk=pk)
    except BlogComment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = BlogCommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     delete blog
@api_view(['DELETE'])
@login_required
def api_delete_blog(request, pk):
    try:
        blog = Podcast_Blog.objects.get(pk=pk)
    except Podcast_Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        operation = blog.delete()
        data = {}
        if operation:
            data["success"] = "delete successful"
        else:
            data["failure"] = "delete failed"
        return Response(data=data)

#delete comment
@api_view(['DELETE'])
@login_required
def api_delete_comment(request, pk):
    try:
        comment = BlogComment.objects.get(pk=pk)
    except BlogComment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        operation = comment.delete()
        data = {}
        if operation:
            data["success"] = "delete successful"
        else:
            data["failure"] = "delete failed"
        return Response(data=data)
