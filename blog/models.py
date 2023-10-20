from django.db import models

# Create your models here.

from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    author = models.ForeignKey(User, models.CASCADE, related_name='post_author')


class Comment(models.Model):
    content = models.TextField(max_length=200)
    date_created = models.DateTimeField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')


class Like(models.Model):
    likes_types = (("H", "Heart"), ('T', "Thumbs up"), ('W', "WOW"), ('A', 'Angry'))
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_likes')
    type = models.CharField(max_length=100, choices=likes_types)


