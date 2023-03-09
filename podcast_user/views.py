from django.contrib.auth import login,logout
from django.shortcuts import render, redirect,get_object_or_404,reverse
from .forms import CustomUserCreationForm, CustomAuthenticationForm,UserEditForm,PasswordForm,UserInfoForm
from .models import PodcastUser, UserInfo,Country
from datetime import datetime, timedelta,date
from django.contrib.auth.decorators import login_required
from podcast_blog.models import Podcast_Blog,BlogComment
from django.contrib import messages
from django_filters import rest_framework as filters
from django import forms
from django.forms.widgets import DateInput, MultiWidget
from django.views.generic import DeleteView,DetailView

class DateRangeWidget(MultiWidget):
    def __init__(self, attrs=None):
        widgets = (
            DateInput(attrs={'type': 'date'}),
            DateInput(attrs={'type': 'date'}),
        )
        super().__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.start, value.stop]
        return [None, None]


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

class CountryFilter(filters.FilterSet):
    class Meta:
        model = Country
        fields = ['country_name']

class PodcastUserFilter(filters.FilterSet):
    first_name = filters.CharFilter(lookup_expr='icontains', label='First Name', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter first name...'}))
    last_name = filters.CharFilter(lookup_expr='icontains', label='Last Name', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter last name...'}))
    email = filters.CharFilter(lookup_expr='icontains', label='Email',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter email...'}))
    username = filters.CharFilter(lookup_expr='icontains', label='Username', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter username...'}))
    date_of_birth = filters.DateFilter(field_name='date_of_birth', lookup_expr='exact', widget=DateInput(attrs={'class': 'form-control','type': 'date'}))
    birthday_range = filters.DateFromToRangeFilter(field_name='date_of_birth', widget=DateRangeWidget(),
                                                   label='Birthday range')
    country = filters.ModelChoiceFilter(field_name='country', queryset=Country.objects.all(),
                                        widget=forms.Select(attrs={'class': 'form-control','required': False}))
class Meta:
        model = PodcastUser
        fields = ['first_name', 'last_name', 'email','username','date_of_birth','birthday_range','country']
@login_required
def users_list(request):
    users = PodcastUser.objects.all().order_by('last_name')
    user_filter = PodcastUserFilter(request.GET, queryset=PodcastUser.objects.all().order_by('last_name'))
    context = {'users': users,'user_filter':user_filter}
    return render(request, 'pages/users/contacts.html', context)
#
# @login_required
# def user_detail(request, user_id):
#     user = get_object_or_404(PodcastUser, user_id=self.kwargs['pk'])
#     try:
#         user_info = UserInfo.objects.get(user=user)
#     except UserInfo.DoesNotExist:
#         user_info = ''
#     blogs = Podcast_Blog.objects.filter(blog_user=user).order_by('-time_of_blog')
#     blog_comments = []
#     for blog in blogs:
#         comments = BlogComment.objects.filter(blog=blog).order_by('-time_of_comment')
#         blog_comments.append((blog, comments))
#
#     followers_count = user.followers.count()
#     following_count = user.following.count()
#     context = {
#         'user': user,
#         'followers_count': followers_count,
#         'following_count': following_count,
#         'user_info': user_info,
#         'blog_comments': blog_comments,
#     }
#     return render(request, 'pages/users//user_detail.html', context)

class User_Detail_View(DetailView):
    model = PodcastUser
    template_name = 'pages/users/user_detail.html'
    def get_context_data(self, *args, **kwargs):
        context = super(User_Detail_View, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(PodcastUser, user_id=self.kwargs['pk'])
        try:
            user_info = UserInfo.objects.get(user=page_user)
        except UserInfo.DoesNotExist:
            user_info = ''
        blogs = Podcast_Blog.objects.filter(blog_user=page_user).order_by('-time_of_blog')
        blog_comments = []
        for blog in blogs:
            comments = BlogComment.objects.filter(blog=blog).order_by('-time_of_comment')
            blog_comments.append((blog, comments))
        followers_count = page_user.followers.count()
        following_count = page_user.following.count()
        # context["page_user"] = page_user
        context = {
            'page_user': page_user,
            'followers_count': followers_count,
            'following_count': following_count,
            'user_info': user_info,
            'blog_comments': blog_comments,
        }
        return context


@login_required
def follow_user(request, pk):
    user_to_follow = get_object_or_404(PodcastUser, user_id=pk)
    request.user.followers.add(user_to_follow)
    messages.success(request, f"You now follow new user!")
    return redirect('users_list')

@login_required
def unfollow_user(request, pk):
    user_to_unfollow = get_object_or_404(PodcastUser, user_id=pk)
    request.user.followers.remove(user_to_unfollow)
    messages.success(request, f"You unfollow user, are you sure about that?!")
    return redirect('users_list')