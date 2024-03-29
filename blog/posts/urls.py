from django.urls import path

from . import views

app_name = "posts"

urlpatterns = [
    path("", views.index, name="index"),  # адрес главной страницы
    path(
        "group/<slug:slug>/edit/", views.group_edit, name="group_edit"
    ),  # адрес страницы редактирования группы
    path(
        "group/<slug:slug>/", views.group_posts, name="group_post"
    ),  # адрес страницы группы
    path(
        "profile/<str:username>/", views.profile, name="profile"
    ),  # адрес страницы профиля
    path(
        "posts/<int:post_id>/comment/",
        views.add_comment,
        name="add_comment"
    ),  # добавление коментария к посту
    path(
        "posts/<int:post_id>/edit/", views.post_edit, name="post_edit"
    ),  # адрес редактирования собственного поста
    path(
        "posts/<int:post_id>/", views.post_detail, name="post_detail"
    ),  # адрес просмотра поста
    path(
        "create/group_post/<slug:slug>/",
        views.new_group_post,
        name="group_post_create"
    ),  # адрес создания поста в группе
    path(
        "create/",
        views.post_create,
        name="post_create"
    ),  # адрес создания поста
    path(
        "group_create/", views.group_create, name="group_create"
    ),  # адрес создания группы
    path(
        "authors_following/",
        views.following_authors,
        name="following_authors"
    ),  # список авторов на которых подписан пользователь
    path("authors/", views.authors, name="authors"),  # все авторы
    path("groups/", views.groups, name="groups"),  # все группы
    # посты подписок пользователя
    path("follow/", views.index_follow, name="follow_index"),
    path(
        "profile/<str:username>/follow/",
        views.profile_follow,
        name="profile_follow"
    ),  # подписка на пользователя
    path(
        "profile/<str:username>/unfollow/",
        views.profile_unfollow,
        name="profile_unfollow",
    ),  # отписка от пользователя
]
