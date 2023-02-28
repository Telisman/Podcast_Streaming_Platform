from django.shortcuts import render,redirect
from .models import Podcast_Blog,BlogComment
from datetime import datetime, timedelta,date
from django.db.models import Count
from .forms import BlogForm,BlogCommentForm
from django.views.generic import CreateView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import View
from .models import Podcast_Blog
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required





class PodcastBlogCreateView(CreateView):
        queryset = Podcast_Blog.objects.all()
        form_class = BlogForm
        success_url = reverse_lazy('profile_page')
        template_name = 'pages/blog/add_blog.html'

        def get_form_kwargs(self):
            kwargs = super().get_form_kwargs()
            kwargs.update({'user_id': self.request.user.user_id})
            return kwargs


class BlogDeleteView(LoginRequiredMixin,View):
    def post(self, request, *args, **kwargs):
        blog = get_object_or_404(Podcast_Blog, pk=kwargs['pk'])
        if blog.blog_user != request.user:
            # If the user is not the author of the blog post, deny access.
            return redirect('timeline')
        blog.delete()
        return redirect('timeline')

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
    if request.method == 'POST':
        comment_form = BlogCommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.comment_user = request.user
            comment.blog = get_object_or_404(Podcast_Blog, id=request.POST.get('blog_id'))
            comment.save()
            return redirect('timeline')
    else:
        comment_form = BlogCommentForm()

    context = {
        'blog_comments': blog_comments,
        'sort_by_likes': sort_by_likes,
        'from_date': from_date,
        'to_date': to_date,
        'comment_form': comment_form,

    }
    return render(request, "pages/blog/blog_timeline.html",context)


def like_blog(request, blog_id):
    blog = Podcast_Blog.objects.get(id=blog_id)
    if request.user.is_authenticated:
        blog.like(request.user)
    return redirect('timeline')


def unlike_blog(request, blog_id):
    blog = Podcast_Blog.objects.get(id=blog_id)
    if request.user.is_authenticated:
        blog.unlike(request.user)
    return redirect('timeline')