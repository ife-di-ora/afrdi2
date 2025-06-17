from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("news", views.news, name="news"),
    path("research", views.research, name="research"),
    path("publications", views.publications, name="publications"),
    path("contact", views.contact, name="contact us"),
    path("about", views.about, name="about"),
]