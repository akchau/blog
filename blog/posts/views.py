from django.shortcuts import render, get_object_or_404
from .models import Post, Group

def index(request):
    template = 'posts/index.html'
    title = 'Главная'
    header = 'Лента новостей'
    posts = Post.objects.order_by('-pub_date')[:10]
    context ={
        'title': title,
        'header': header,
        'posts': posts,
    }
    return render(request, template, context)

def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    template = 'posts/group_list.html'
    title = 'группа'
    header = f'Записи группы {group.title}'
    context ={
        'title': title,
        'header': header,
        'posts': posts,
    }
    return render(request, template, context)
    


