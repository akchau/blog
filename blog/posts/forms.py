from .models import Group, Post, Comment
from django import forms


class PostForm(forms.ModelForm):
    """Форма для создания и редактирования поста"""
    class Meta:
        model = Post
        fields = (
            "text",
            "image",
        )


class GroupForm(forms.ModelForm):
    """Форма для создания и редактирования группы"""
    class Meta:
        model = Group
        fields = (
            "image",
            "title",
            "slug",
            "description",
        )


class CommentForm(forms.ModelForm):
    """Форма для создания и редактирования коммента"""
    class Meta:
        model = Comment
        fields = ("text",)
