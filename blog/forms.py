from django import forms
from .models import Post


class NewPostFrom(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'author', 'status']

