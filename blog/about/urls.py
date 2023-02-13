from django.urls import path
from . import views


app_name = "about"

urlpatterns = [
    # сайт с контактами
    path("contact/", views.ContactPage.as_view(), name="contact"),
    # сайт с описанными технологиями
    path("tech/", views.TechPage.as_view(), name="tech"),
]
