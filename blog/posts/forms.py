from .models import Group, Post
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group', 'image',)


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('image', 'title', 'slug', 'description',)
