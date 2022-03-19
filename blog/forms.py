from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class UserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('username','email')



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'content','image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'content': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }
        


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', 'author')

        labels = {
            'text':'Comment',
            'author':'Name'
        }
