from django.forms import ModelForm
from .models import EmailMessage
from django import forms

class SendEmail(ModelForm):
    class Meta:
        model = EmailMessage
        fields = ('name','email','subject','message')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }