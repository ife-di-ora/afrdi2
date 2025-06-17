from django.shortcuts import render
# from django.http import HttpResponse
from .models import News, Mission, Vision, Publications, Research

# Create your views here.

def index(request):
    news = News.objects.order_by("-pub_date")[:5]
    print (news)
    content = {'news': news}
    return render (request, 'home_app/index.html', content)

def news(request):
    news = News.objects.all()
    content = {'news': news}
    return render (request, 'home_app/news.html', content)

def about(request):
    mission = Mission.objects.all()
    vision = Vision.objects.all()
    content = {'mission': mission, 'vision': vision}
    return render (request, 'home_app/about.html', content)

def contact(request):
    return render (request, 'home_app/contact.html')

def publications(request):
    publications = Publications.objects.all()
    content = {'publications': publications}
    return render (request, 'home_app/publications.html', content)

def research(request):
    research = Research.objects.all()
    content = {'research': research}
    return render (request, 'home_app/research.html', content)

