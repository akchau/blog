from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CreationForm
from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404, redirect
from .forms import Feedback
from django.core.mail import mail_admins, send_mail

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

def feedback(request):
    form = Feedback(request.POST or None)
    if form.is_valid():
        subject = form.cleaned_data['subject']
        body = (
            form.cleaned_data['message'],
            form.cleaned_data['email']
        )
        message = "\n".join(body)
        send_mail(subject, message, 'webmaster@localhost', ['gleb.lazarev20@yandex.ru'], fail_silently=False)
        return redirect('users:cabinet', username=request.user)
    template = 'posts/form_post.html'
    context = {
        'title': 'Обратная связь',
        'action': 'Обратная связь',
        'form': form
    }
    return render(request, template, context)
