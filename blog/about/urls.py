from django.urls import path
from . import views


app_name = "about"

urlpatterns = [
    path("contact/", views.ContactPage.as_view(), name="contact"),
    path("tech/", views.TechPage.as_view(), name="tech"),
]
