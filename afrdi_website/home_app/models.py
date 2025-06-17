from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

class News(models.Model):
    title = models.CharField(max_length = 300)
    pub_date = models.DateTimeField ('date published')
    text = models.CharField(max_length = 5000)
    pic = models.ImageField(upload_to="news_image")

    def __str__(self):
        return self.title

class Publications (models.Model):
    title = models.CharField(max_length = 300)
    pub_date = models.DateTimeField ('date published')
    description = models.CharField(max_length = 1000)
    doc = models.FileField(upload_to='docs')

    
    def __str__(self):
        return self.title
    

class Mission(models.Model):
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text
    
    def clean(self):
        if Mission.objects.exists() and not self.pk:
            raise ValidationError("You can only have one Mission")

class Vision(models.Model):
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text
    
    def clean(self):
        if Vision.objects.exists() and not self.pk:
            raise ValidationError("You can only have one Vision")


class HomeCarousel(models.Model):
    title = models.CharField(max_length=200)
    caption = models.CharField(max_length=200)
    image = models.ImageField(upload_to="media")

class Research (models.Model):
    title = models.CharField(max_length = 300)
    description = models.CharField(max_length = 1000)
    
    def __str__(self):
        return self.title
    

