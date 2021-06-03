from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    body = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title

    def snippet(self):
        snippet = self.body[:15] + '......................'
        return snippet

    def get_absolute_url(self):
        return reverse


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)


    
    def get_absolute_url(self):
        return reverse