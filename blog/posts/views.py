from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from .models import Post, Group, Comment
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import PostForm, GroupForm, GroupPostForm, CommentForm

User = get_user_model()


def get_page_obj(request, models):
    paginator = Paginator(models, 10)
    page_number = request.GET.get('page')
    page_obj =paginator.get_page(page_number)
    return page_obj


def index(request):
    posts = Post.objects.order_by('-pub_date')
    page_obj = get_page_obj(request, posts)
    template = 'posts/index.html'
    title = 'Главная'
    header = 'Лента новостей'
    subheader = 'Все записи пользователей'
    context ={
        'title': title,
        'header': header,
        'subheader': subheader,
        'page_obj': page_obj,
    }
    return render(request, template, context)

def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')
    page_obj = get_page_obj(request, posts)
    template = 'posts/group_post.html'
    title = group.title
    header = title
    post_count = group.posts.count()
    subheader = f'{group.description} Всего записей - {post_count}'
    context ={
        'title': title,
        'header': header,
        'subheader': subheader,
        'page_obj': page_obj,
        'group': group
    }
    return render(request, template, context)

def profile(request, username):
    author = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=author).order_by('-pub_date')
    post_count = author.posts.count()
    page_obj = get_page_obj(request, posts)
    template = 'posts/index.html'
    title = author.get_full_name
    header = author.get_full_name
    subheader =f'Всего постов: {post_count}'
    context ={
        'title': title,
        'header': header,
        'subheader': subheader,
        'page_obj': page_obj,
    }
    return render(request, template, context)


def post_detail(request, post_id):
    template = 'posts/post_detail.html'
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post)
    page_obj = get_page_obj(request, comments)
    form = CommentForm()
    title = f'Пост'
    header = f'Пост пользователя {post.author.username}'
    subheader = f'Детальная информация поста'
    context ={
        'title': title,
        'header': header,
        'subheader': subheader,
        'post': post,
        'page_obj': page_obj,
        'form': form
    }
    return render(request, template, context)


@login_required
def post_create(request):
    form = PostForm(
        request.POST or None,
        files=request.FILES or None,
    )
    if form.is_valid():
        new_post = form.save(commit=False)
        new_post.author = request.user
        form.save(commit=True)
        return redirect('posts:profile', username=request.user)
    template = 'posts/post_create.html'
    title = 'Новый пост'
    header = 'Новый пост'
    subheader = 'Создайте новый пост'
    action = 'Создайте новый пост'
    context = {
        'title': title,
        'header': header,
        'subheader': subheader,
        'form': form,
        'action': action
    }
    return render(request, template, context)


@login_required
def group_create(request):
    form = GroupForm(
        request.POST or None,
        files=request.FILES or None,
    )
    if form.is_valid():
        new_group = form.save(commit=False)
        new_group.main_admin = request.user
        form.save(commit=True)
        return redirect('posts:group_post', form.cleaned_data['slug'])
    template = 'posts/group_create.html'
    title = 'Новая группа'
    header = title
    subheader = 'Создайте новую группу'
    action = 'Укажите данные группы'
    context = {
        'title': title,
        'header': header,
        'subheader': subheader,
        'form': form,
        'action': action
    }
    return render(request, template, context)


@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user != post.author:
        return redirect('posts:post_detail', post_id=post_id)
    form = PostForm(
        request.POST or None,
        files=request.FILES or None,
        instance=post,
    )
    if form.is_valid():
        form.save()
        return redirect('posts:post_detail', post_id=post.id)
    title = 'Редактирование поста'
    header = 'Редактирование поста'
    subheader = 'Для редактирования поста заполните форму ниже'
    action = 'Редактируйте запись'
    template = 'posts/post_create.html'
    context = {
        'title': title,
        'header': header,
        'subheader': subheader,
        'action': action,
        'form': form,
        'is_edit': True,
        'post_id': post_id
    }
    return render(request, template, context)


@login_required
def group_edit(request, slug):
    group = get_object_or_404(Group, slug=slug)
    if request.user != group.main_admin:
        return redirect('posts:group_post', slug=slug)
    form = GroupForm(
        request.POST or None,
        files=request.FILES or None,
        instance=group,
    )
    if form.is_valid():
        form.save()
        return redirect('posts:group_post', slug=slug)
    title = 'Редактирование группы'
    header = 'Редактирование группы'
    subheader = 'Для редактирования группы заполните форму ниже'
    action = 'Редактируйте группу'
    template = 'posts/group_create.html'
    context = {
        'title': title,
        'header': header,
        'subheader': subheader,
        'action': action,
        'form': form,
        'is_edit': True,
        'slug': group.slug
    }
    return render(request, template, context)


@login_required
def add_comment(request, post_id):
    form = CommentForm(request.POST or None)
    post = get_object_or_404(Post, pk=post_id)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
    return redirect('posts:post_detail', post_id=post_id)


def authors(request):
    authors = get_list_or_404(User)
    page_obj = get_page_obj(request, authors)
    template = 'posts/authors.html'
    title = 'Все пользователи'
    header = 'Все пользователи'
    subheader ='Все пользователи сайта'
    context ={
        'title': title,
        'header': header,
        'subheader': subheader,
        'page_obj': page_obj,
    }
    return render(request, template, context)


def groups(request):
    groups = get_list_or_404(Group)
    page_obj = get_page_obj(request, groups)
    template = 'posts/groups.html'
    title = 'Группы'
    header = 'Все группы'
    subheader ='Все группы сайта'
    context ={
        'title': title,
        'header': header,
        'subheader': subheader,
        'page_obj': page_obj,
    }
    return render(request, template, context)


def new_group_post(request, slug):
    group = get_object_or_404(Group, slug=slug)
    form = GroupPostForm(
        request.POST or None,
        files=request.FILES or None,
    )
    if form.is_valid():
        new_post = form.save(commit=False)
        new_post.group = group
        new_post.author = request.user
        form.save(commit=True)
        return redirect('posts:group_post', slug=group.slug)
    template = 'posts/group_post_create.html'
    title = f'Новый пост для сообщества: {group.title}'
    header = f'Новый пост для сообщества: {group.title}'
    subheader = f'Создайте новый пост для сообщества: {group.title}'
    action = 'Создайте новый пост'
    context = {
        'title': title,
        'header': header,
        'subheader': subheader,
        'form': form,
        'action': action,
        'slug': slug
    }
    return render(request, template, context)