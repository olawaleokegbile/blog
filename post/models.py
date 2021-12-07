from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField

# Create your models here.
class Post(models.Model):
    image = CloudinaryField('image')
    title = models.CharField(max_length=100)
    body = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        ordering = ['-created_at']

class Comment(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=70,blank=True,unique=True)
    message = models.TextField()
    
    def __str__(self):
        return self.name