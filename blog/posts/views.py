from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, Group
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator


def index(request):
    template = 'posts/index.html'
    title = 'Главная'
    header = 'Лента новостей'
    posts = Post.objects.order_by('-pub_date')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context ={
        'title': title,
        'header': header,
        'page_obj': page_obj,
    }
    return render(request, template, context)

def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template = 'posts/index.html'
    title = group.title
    header = f'Записи группы {title}'
    context ={
        'title': title,
        'header': header,
        'page_obj': page_obj,
    }
    return render(request, template, context)
    
def profile(request, username):
    User = get_user_model()
    author = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=author).order_by('-pub_date')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template = 'posts/index.html'
    title = author.get_full_name
    header = author.get_full_name
    context ={
        'title': title,
        'header': header,
        'page_obj': page_obj,
    }
    return render(request, template, context)

def post_edit(request, post_id):
    return HttpResponse('Страница редактирования поста')

def post_detail(request, post_id):
    return HttpResponse('Страница поста')

def post_create(request):
    return HttpResponse('Страница создания поста')
