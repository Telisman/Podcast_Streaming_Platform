from django import forms
from .models import Podcast_Blog
from podcast_user.models import PodcastUser

class BlogForm(forms.ModelForm):
    model = Podcast_Blog
    fields = ('name', 'blog_text')
    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'blog_text': forms.Textarea(attrs={'class': 'form-control'}),
    }

    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop("user_id")
        super().__init__(*args, **kwargs)
        self.fields['blog_user'].initial = user_id

    class Meta:
        model = Podcast_Blog
        fields = ('name', 'blog_text', 'blog_user')
        widgets = {
            'blog_user': forms.HiddenInput(),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'blog_text': forms.Textarea(attrs={'class': 'form-control'}),
        }

