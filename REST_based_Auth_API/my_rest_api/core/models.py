from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    text_post = models.CharField(max_length=500)

    def __str__(self):
        return self.text_post
