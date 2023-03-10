from rest_framework import serializers
from.models import Podcast_Blog,BlogComment
from podcast_user.serializers import PodcastUserSerializer



class BlogCommentSerializer(serializers.ModelSerializer):
    comment_user = PodcastUserSerializer(read_only=True)

    class Meta:
        model = BlogComment
        fields = ['id', 'blog', 'comment_text', 'comment_user', 'time_of_comment']


class Podcast_BlogSerializer(serializers.ModelSerializer):
    blog_user = PodcastUserSerializer(read_only=True)
    comments = BlogCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Podcast_Blog
        fields = ['id', 'name', 'time_of_blog', 'blog_text', 'blog_user', 'likes', 'comments']