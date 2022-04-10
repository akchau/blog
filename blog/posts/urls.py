from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'), # адрес главной страницы
    path('group/<slug:slug>/', views.group_posts, name='group_post'), # адрес страницы группы
    path('profile/<str:username>/', views.profile, name='profile'), # адрес страницы профиля
    path('posts/<int:post_id>/edit/', views.post_edit, name='post_edit'), # адрес редактирования собственного поста
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'), # адрес просмотра поста
    path('create/', views.post_create, name='post_create'), # адрес создания поста
]