from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth import get_user_model
from django.db import models

from likes.models import Like

User = get_user_model()


class Post(models.Model):
    body = models.CharField(max_length=140)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = GenericRelation(Like)

    def __str__(self):
        return self.body

    @property
    def total_likes(self):
        return self.likes.count()
