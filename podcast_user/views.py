from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect,get_object_or_404
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from .models import PodcastUser
from datetime import datetime, timedelta
from django.views.generic import ListView


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



def FAQ(request):
    return render(request,'pages/faq.html')


#
# class PodcastDashboard(ListView):
#     model = PodcastUser
#     template_name = "pages/users/podcast_dashboard.html"
#     context_object_name = 'profile'
#
#     def get_queryset(self):  # get_queryset biblioteka iz paythona
#         return PodcastUser.objects.all()




# def test(request):
#     form = CustomUserCreationForm()
#     return render(request, 'pages/test.html', {'form': form})

