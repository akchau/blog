from django.shortcuts import render
from .models import Post

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
    template = 'posts/group_list.html'
    title = 'группа'
    header = 'Записи группы'
    posts = Post.objects.order_by('-pub_date')[:10]
    context ={
        'title': title,
        'header': header,
        'posts': posts,
    }
    return render(request, template, context)
    


