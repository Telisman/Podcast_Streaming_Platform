from django import forms
from .models import Podcast_Blog

class Add_New_Blog(forms.ModelForm):
    class Meta:
        model = Podcast_Blog
        fields = ['name', 'blog_text']
        labels = {
            'name': 'name',
            'blog_text': 'blog_text',
        }
        widgets = {
            'blog_text': forms.Textarea(attrs={'rows': 15, 'required': True}),
            'name': forms.TextInput(attrs={'placeholder': 'e.g. English, French','required': True}),
        }

class DeleteBlogForm(forms.Form):
    blog_id = forms.IntegerField()


class EditBlogForm(forms.ModelForm):
    class Meta:
        model = Podcast_Blog
        fields = ['name', 'blog_text']
