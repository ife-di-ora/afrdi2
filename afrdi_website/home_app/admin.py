from django.contrib import admin

# Register your models here.
from .models import News, Publications, Mission, Vision, HomeCarousel, Staff, Research

admin.site.register(News)
admin.site.register(Publications)
admin.site.register(Mission)
admin.site.register(HomeCarousel)
admin.site.register(Vision)
admin.site.register(Staff)
admin.site.register(Research)