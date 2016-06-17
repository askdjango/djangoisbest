from django import forms
from blog.models import Post, Comment
from blog.widgets import GoogleMapPointWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'photo', 'latlng']
        widgets = {
            'latlng': GoogleMapPointWidget,
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'message']

