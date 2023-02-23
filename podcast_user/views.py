from django.contrib.auth import login,logout
from django.shortcuts import render, redirect,get_object_or_404,reverse
from .forms import CustomUserCreationForm, CustomAuthenticationForm,UserEditForm,PasswordForm,UserInfoForm
from .models import PodcastUser, UserInfo
from datetime import datetime, timedelta,date
from django.contrib.auth.decorators import login_required
from podcast_blog.models import Podcast_Blog
from django.contrib import messages

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

    if request.method == 'POST':
        user_form = UserEditForm(request.POST, request.FILES, instance=request.user)
        password_form = PasswordForm(request.user, request.POST)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('profile_page')

        if password_form.is_valid():
            password_form.save()
            messages.success(request, 'Your password has been updated.')
            return redirect('profile_page')

    else:
        user_form = UserEditForm(instance=request.user)
        password_form = PasswordForm(request.user)

    # url = reverse('user:edit_user_info', kwargs={'user_id': request.user.user_id})

    return render(request, 'pages/users/profile.html', {
        'user': request.user,
        'user_info': user_info,
        'blog_posts': blog_posts,
        'like_counts': like_counts,
        'user_form': user_form,
        'password_form': password_form,
        # 'url': url,
    })

@login_required
def edit_user_info(request):
    user_info, created = UserInfo.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserInfoForm(request.POST, instance=user_info)
        if form.is_valid():
            form.save()
            return redirect('profile_page')
    else:
        form = UserInfoForm(instance=user_info, initial={
            'bio': user_info.bio,
             'language': user_info.language,
            'education': user_info.education,
            'skills': user_info.skills,
            'user': user_info.user
        })
    return render(request, 'pages/users/edit_user_info.html', {'form': form})
# def edit_user_info(request, user_id):
#     user = get_object_or_404(PodcastUser, user_id=user_id)
#     user_info = user
#     if request.method == 'POST':
#         form = UserInfoForm(request.POST, instance=user_info)
#         if form.is_valid():
#             form.save()
#             return redirect('profile_page')
#     else:
#         form = UserInfoForm(instance=user_info)
#     return render(request, 'pages/users/edit_user_info.html', {'form': form, 'user': user})



def users_list(request):
    return render(request,'pages/users/contacts.html')