from django.shortcuts import render, get_object_or_404, get_list_or_404
# from django.http import HttpResponse
from .models import News, Mission, Vision, Publications, Research, Staff

# Create your views here.

def index(request):
    news = News.objects.order_by("-pub_date")[:8]
    mission = Mission.objects.first()
    vision = Vision.objects.first()
    research = Research.objects.order_by('-pub_date')[:4]
    content = {'research': research, 'news': news, 'mission': mission, 'vision': vision}
    return render (request, 'home_app/index.html', content)

def news(request, news_id=None):
    if news_id:
        news_detail = get_object_or_404(News, pk=news_id)
        return render (request, 'home_app/news_detail.html', {'news': news_detail})
    else:
        news_list = News.objects.order_by('-pub_date')
        content = {'news': news_list}
        return render (request, 'home_app/news.html', content)

def about(request):
    mission = Mission.objects.first()
    vision = Vision.objects.first()
    staff = Staff.objects.all()
    content = {'mission': mission, 'vision': vision, 'staff': staff}
    
    return render (request, 'home_app/about.html', content)

def contact(request):
    return render (request, 'home_app/contact.html')

def publications(request):
    publications = Publications.objects.all()
    content = {'publications': publications}
    return render (request, 'home_app/publications.html', content)

def research (request, research_id=None):
    if research_id:
        research_detail = get_object_or_404(Research, pk=research_id)
        return render (request, 'home_app/research_detail.html', {'research': research_detail})
    else:
        research_list = Research.objects.order_by('-pub_date')
        content = {'research': research_list}
        return render (request, 'home_app/research.html', content)

  