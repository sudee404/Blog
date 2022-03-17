from django.db import models
from django.utils import timezone
from django.urls import reverse,reverse_lazy
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200,help_text='Enter Post title',unique=True)
    image = models.ImageField(upload_to='images',default='default.png',help_text='Pictures relating to post',null=True)
    content = models.TextField(help_text='Enter Post content')
    author = models.ForeignKey('Author',on_delete=models.CASCADE,null=True)
    publish_date = models.DateField(default=timezone.now)
    tags = models.ForeignKey('Tags',on_delete=models.SET_NULL,null=True)
    
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    
    
    def __str__(self):
        return self.title
    
    
class Author(models.Model):
    name = models.CharField(max_length=200,unique=True)
    pic = models.ImageField(upload_to='pics',default='default.png')
    
    def __str__(self):
        return self.name
    
class Tags(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Team(models.Model):
    name = models.CharField(max_length=200)
    pic = models.ImageField(upload_to='pic')
    position = models.CharField(max_length=200)
    detail = models.TextField()
    
    def __str__(self):
        return self.name