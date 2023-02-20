from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import PodcastUser,Country
from django import forms


class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=17, required=False)
    country = forms.ModelChoiceField(queryset=Country.objects.all(), required=True)
    class Meta:
        model = PodcastUser
        fields = ('email','username', 'first_name', 'last_name', 'phone_number', 'password1', 'password2','country')

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Email')