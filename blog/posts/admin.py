from django.contrib import admin
from .models import Post, Group, Comment


class PostAdmin(admin.ModelAdmin):
    """Отображение в админке постов"""
    list_display = (
        "pk",
        "text",
        "pub_date",
        "author",
        "group",
        "image",
    )
    search_fields = (
        "text",
    )
    list_filter = ("pub_date",)
    empty_value_display = "-пусто-"
    list_editable = (
        "text",
        "group",
        "image",
    )


class GroupAdmin(admin.ModelAdmin):
    """Отображение в админке групп"""
    list_display = (
        "pk",
        "main_admin",
        "image",
        "title",
        "slug",
        "description"
    )
    list_editable = (
        "main_admin",
        "title",
        "description",
        "slug",
    )
    search_fields = (
        "title",
        "description",
    )
    empty_value_display = "-пусто-"


class CommentAdmin(admin.ModelAdmin):
    """Отображение в админке комментов"""
    list_display = (
        "pk",
        "post",
        "author",
        "text",
    )
    list_editable = ("text",)
    search_fields = ("text",)
    empty_value_display = "-пусто-"


admin.site.register(
    Post, PostAdmin
)
admin.site.register(Group, GroupAdmin)
admin.site.register(Comment, CommentAdmin)
