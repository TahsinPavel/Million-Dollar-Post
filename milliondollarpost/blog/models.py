from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default='Million Dollar Post')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    
    def __str__(self):
        return self.title + ' | ' + self.author.username
# Create your models here.
