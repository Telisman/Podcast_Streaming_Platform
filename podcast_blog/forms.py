from django import forms
from .models import Podcast_Blog,BlogComment

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

# class BlogCommentForm(forms.ModelForm):
#     class Meta:
#         model = BlogComment
#         fields = ['comment_text']
#         widgets = {
#             'comment_text': forms.Textarea(attrs={'placeholder': 'Enter your comment here...'})
#         }

class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['comment_text']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(BlogCommentForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        comment = super(BlogCommentForm, self).save(commit=False)
        comment.comment_user = self.user
        if commit:
            comment.save()
        return comment