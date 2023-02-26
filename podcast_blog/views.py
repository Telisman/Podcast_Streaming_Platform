from django.shortcuts import render,redirect
from .models import Podcast_Blog,BlogComment
from datetime import datetime, timedelta,date
from django.db.models import Count
from .forms import EditBlogForm,DeleteBlogForm,Add_New_Blog


def blog_timeline(request):
    username = request.GET.get('username', None)
    from_date = request.GET.get('from_date', None)
    to_date = request.GET.get('to_date', None)
    if from_date and to_date:
        from_date = datetime.strptime(from_date, '%Y-%m-%d').date()
        to_date = datetime.strptime(to_date, '%Y-%m-%d').date()
        blog_posts = Podcast_Blog.objects.filter(time_of_blog__range=[from_date, to_date])
    else:
        one_year_ago = date.today() - timedelta(days=365)
        if username:
            blog_posts = Podcast_Blog.objects.filter(blog_user__username=username, time_of_blog__gte=one_year_ago)
        else:
            blog_posts = Podcast_Blog.objects.filter(time_of_blog__gte=one_year_ago)
    sort_by_likes = request.GET.get('sort_by_likes', None)
    if sort_by_likes:
        blog_posts = blog_posts.annotate(num_likes=Count('likes')).order_by('-num_likes')
    else:
        blog_posts = blog_posts.order_by('-time_of_blog')
    blog_comments = []
    for blog in blog_posts:
        comments = BlogComment.objects.filter(blog=blog).order_by('-time_of_comment')
        blog_comments.append((blog, comments))
    return render(request, "pages/blog/blog_timeline.html",
                  {'blog_comments': blog_comments, 'sort_by_likes': sort_by_likes, 'from_date': from_date,
                   'to_date': to_date})


def add_blog(request):
    if request.method == 'POST':
        form = Add_New_Blog(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.blog_user = request.user  # Assumes you have implemented authentication
            blog.save()
            return redirect('timeline')
    else:
        add_blog_form = Add_New_Blog()
    return render(request, 'pages/users/profile.html', {'add_blog_form': add_blog_form})