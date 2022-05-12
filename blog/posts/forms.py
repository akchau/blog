from .models import Group, Post, Comment
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'image',)


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('image', 'title', 'slug', 'description',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)