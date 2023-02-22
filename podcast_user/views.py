from django.contrib.auth import login,logout
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import PodcastUser, UserInfo
from datetime import datetime, timedelta,date
from django.contrib.auth.decorators import login_required
from podcast_blog.models import Podcast_Blog

def Navbar_footer_menu(request):
    return render(request, "pages/navbar_footer_menu.html", {})

def login_and_register(request):
    if request.method == 'POST':
        register_form = CustomUserCreationForm(request.POST)
        login_form = CustomAuthenticationForm(request, data=request.POST)
        if register_form.is_valid():
            user = register_form.save()
            login(request, user)
            return redirect('login_and_register')
        elif login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('podcast_dashboard')
    else:
        register_form = CustomUserCreationForm()
        login_form = CustomAuthenticationForm()
    return render(request, 'pages/login_and_register.html', {'register_form': register_form, 'login_form': login_form})


def logout_view(request):
    logout(request)
    return redirect('login_and_register')


def PodcastDashboard(request):
    thirty_days_ago = datetime.now() - timedelta(days=30)
    new_users = PodcastUser.objects.filter(date_of_join__gte=thirty_days_ago)
    return render(request, 'pages/users/podcast_dashboard.html',{'new_users': new_users})


@login_required
def profile_page(request):
    try:
        user_info = UserInfo.objects.get(user=request.user)
    except UserInfo.DoesNotExist:
        user_info = None

    one_year_ago = date.today() - timedelta(days=365)
    blog_posts = Podcast_Blog.objects.filter(blog_user=request.user, time_of_blog__gte=one_year_ago).order_by(
        '-time_of_blog')
    like_counts = []
    for post in blog_posts:
        like_counts.append(post.likes.count())

    return render(request, 'pages/users/profile.html',{'user': request.user, 'user_info': user_info, 'blog_posts': blog_posts, 'like_counts':like_counts})


def users_list(request):
    return render(request,'pages/users/contacts.html')