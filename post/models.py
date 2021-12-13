from typing_extensions import Required
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)
    body = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, related_name='replies', on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return str(self.post)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    
    def __str__(self):
        return self.name