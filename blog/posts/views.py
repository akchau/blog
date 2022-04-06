from django.shortcuts import render

def index(request):
    template = 'posts/index.html'
    title = 'Главная'
    header = 'Все записи'
    context ={
        'title': title,
        'header': header,
    }
    return render(request, template, context)

def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = 'группа'
    header = 'Записи группы'
    context ={
        'title': title,
        'header': header,
    }
    return render(request, template, context)
    


