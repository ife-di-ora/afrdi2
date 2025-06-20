from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("news/<int:news_id>", views.news, name="news"),
    path("news", views.news, name="news"),
    path("research", views.research, name="research"),
    path("research/<int:research_id>", views.research, name="research"),
    path("publications", views.publications, name="publications"),
    path("contact", views.contact, name="contact us"),
    path("about", views.about, name="about"),
]