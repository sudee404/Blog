from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200,help_text='Enter Post title',unique=True)
    image = models.ImageField(upload_to='images',default='default.png',help_text='Pictures relating to post',null=True)
    content = models.TextField(help_text='Enter Post content')
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    create_date = models.DateField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True,null=True)
    
    

    def publish(self):
        self.publish_date = timezone.now()
        self.save()
    
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    
    
    def __str__(self):
        return self.title
    
import uuid
class PostInstance(models.Model):
    """model representing particular instance of a post that is to be starred"""
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,help_text="unique id for this specific post")
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    starrer = models.ForeignKey('auth.User',on_delete=models.SET_NULL,null=True)
    starred = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ['post','starrer']    
        
    def star(self,request):
        self.starred = True
        self.starrer = request.user
        self.save()
    
    def __str__(self):
        return self.post.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=200,default='Anonymous')
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    
        
    def get_absolute_url(self):
        return reverse("post-list")
    
    def __str__(self):
        return self.text
    

    
class Team(models.Model):
    name = models.CharField(max_length=200)
    pic = models.ImageField(upload_to='pic')
    position = models.CharField(max_length=200)
    detail = models.TextField()
    
    def __str__(self):
        return self.name

class Author(models.Model):
    user = models.OneToOneField('auth.User',on_delete=models.CASCADE)
    pic = models.ImageField(upload_to='pic',default='default.png',null=True, blank=True)
   
    
    def __str__(self):
        return self.user.username
    