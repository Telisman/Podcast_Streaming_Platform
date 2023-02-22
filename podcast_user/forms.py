from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,UserChangeForm,PasswordChangeForm
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




class UserEditForm(UserChangeForm):
    password = None

    class Meta:
        model = PodcastUser
        fields = ('first_name', 'last_name', 'phone_number', 'address', 'city_name', 'postal_code', 'image')

class PasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label="Old Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(label="New Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = PodcastUser
        fields = ('old_password', 'new_password1', 'new_password2')