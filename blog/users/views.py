from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CreationForm, EditName
from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404, redirect
from .forms import Feedback
from django.core.mail import mail_admins, send_mail
from django.contrib.auth.decorators import login_required


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/signup.html'


@login_required
def edit_name(request, username):
    User = get_user_model()
    author = get_object_or_404(User, username=username)
    form = EditName(request.POST or None, instance=author)
    if form.is_valid():
        first_name = form.cleaned_data['first_name']
        form.save()
        return redirect('users:cabinet', username=username)
    template = 'users/edit_param.html'
    context = {
        'title': 'Изменить имя',
        'header': 'Изменить имя',
        'action': 'Введите имя',
        'form': form,
        'namespace': 'users:edit_name'
    }
    return render(request, template, context)

@login_required
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
        'header': 'Обратная связь',
        'action': 'Введите ваше сообщение',
        'form': form,
        'namespace': 'users:feedback'
    }
    return render(request, template, context)
