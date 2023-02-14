from django.shortcuts import render
from http import HTTPStatus


def page_not_found(request, exception):
    """Функция выводит шаблон кастомной ошибки не найден"""
    template = "core/404.html"
    context = {
        "path": request.path,
        "title": "Ошибка 404",
        "header": "Ошибка 404",
    }
    return render(request, template, context, status=HTTPStatus.NOT_FOUND)


def csrf_failure(request, reason=""):
    """Функция выводит шаблон кастомной ошибки csrf-токена"""
    return render(request, "core/403csrf.html")


def bad_request(request, exception):
    """Функция кастомной ошибки неверный запрос"""
    template = "core/404.html"
    context = {
        "path": request.path,
        "title": "Ошибка 400",
        "header": "Ошибка 400",
    }
    return render(request, template, context, status=HTTPStatus.BAD_REQUEST)


def forbidden(request, exception):
    """Функция кастомной ошибки нет доступа"""
    template = "core/404.html"
    context = {
        "path": request.path,
        "title": "Ошибка 403",
        "header": "Ошибка 403",
    }
    return render(request, template, context, status=HTTPStatus.FORBIDDEN)


def server_error(request):
    """Функция кастомной ошибки ошибка сервера"""
    template = "core/404.html"
    context = {
        "path": request.path,
        "title": "Ошибка 500",
        "header": "Ошибка 500",
    }
    return render(
        request, context, template, status=HTTPStatus.INTERNAL_SERVER_ERROR)
