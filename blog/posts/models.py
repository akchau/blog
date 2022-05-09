from django.db import models
from django.contrib.auth import get_user_model
from core.models import CreatedModel

User = get_user_model()


class Group(models.Model):
    """Модель группы."""
    title = models.CharField(
        'Название группы',
        max_length=200,
        help_text='Укажите название группы',
    )
    slug = models.SlugField(
        'Адресс группы',
        max_length=200,
        unique=True,
        help_text='Укажите адресс группы',
    )
    description = models.TextField(
        'Описание группы',
        help_text='Опишите группу',
    )
    image = models.ImageField(
        'Аватвр сообщества',
        upload_to='posts/',
        blank=True,
    )
    main_admin = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='community',
        verbose_name='Создатель',
    )
    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
    def __str__(self):
        return self.title


class Post(CreatedModel):
    """Модель поста."""
    text = models.TextField(
        'Текст поста',
        help_text='Напишите текст поста'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор',
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='posts',
        verbose_name='Группа',
        blank=True,
        null=True,
        help_text='Выберите группу',
    )
    image = models.ImageField(
        'Картинка',
        upload_to='posts/',
        blank=True,
    )
    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
    def __str__(self):
        return self.text[:15]
