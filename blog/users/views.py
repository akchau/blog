from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CreationForm
from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404

class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/signup.html'

def cabinet(request, username):
    User = get_user_model()
    author = get_object_or_404(User, username=username)
    title = 'Личный кабинет'
    header = 'Личный кабинет'
    template = 'users/cabinet.html'
    context ={
        'title': title,
        'header': header,
    }
    return render(request, template, context)
