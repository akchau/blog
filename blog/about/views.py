from django.views.generic.base import TemplateView
from dataclasses import dataclass


@dataclass
class InfoView:
    """Представление информационной странницы
    основано на @dataclass
    """

    header: str
    text: dict


class ContactPage(TemplateView):
    """Страница О себе."""
    template_name = "about/info_page.html"

    def get_context_data(self, **kwargs):
        """Метод для создания контекста"""
        context = super().get_context_data(**kwargs)
        content = InfoView
        content.header = "Об авторе"
        content.text = "Я Глеб"
        context["title"] = "Контактная информация"
        context["header"] = "Контактная информация"
        context["content"] = content
        return context


class TechPage(TemplateView):
    """Страница Технологии."""
    template_name = "about/info_page.html"

    def get_context_data(self, **kwargs):
        """Метод для создания контекста"""
        context = super().get_context_data(**kwargs)
        content = InfoView
        content.header = "Технологии"
        content.text = "Django"
        context["title"] = "Технологии"
        context["header"] = "Технологии"
        context["content"] = content
        return context
