from django.shortcuts import render
from .models import Podcast_Blog,BlogComment
from datetime import datetime, timedelta,date



def blog_timeline(request):
    one_year_ago = date.today() - timedelta(days=365)
    blog_posts = Podcast_Blog.objects.filter(blog_user=request.user, time_of_blog__gte=one_year_ago).order_by(
        '-time_of_blog')
    return render(request, "pages/blog/blog_timeline.html", {})