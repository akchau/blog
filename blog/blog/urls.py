"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin # импортируем чтобы указать обработчик из библиотеки django.contrib
from django.urls import path, include # необходимые методы управления адресамии в Django

urlpatterns = [
    path('', include('posts.urls', namespace='posts')), # путь до главной страницы в нем ищутся все адреса
    path('admin/', admin.site.urls, name='admin'), # путь до старниц приложения admin-зоны
    path('auth/', include('users.urls', namespace='users')), # путь для управления пользователем кастомный
    path('auth/', include('django.contrib.auth.urls')), # путь для управления пользователем стандартный если не нашлось ничего в кастомном
    path('about/', include('about.urls', namespace='about'))
]

handler404 = 'core.views.page_not_found'
handler400 = 'core.views.bad_request'
handler403 = 'core.views.forbidden'
handler500 = 'core.views.server_error'



