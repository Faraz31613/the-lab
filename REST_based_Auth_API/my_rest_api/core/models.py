from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import related
from django.http import request


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text_post = models.CharField(max_length=500)

    def __str__(self):
        return self.text_post

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    comment = models.CharField(max_length=300)

    def __str__(self):
        return self.comment

class Request(models.Model):

    class Status:
        PENDING = 'P'
        ACCEPTED = 'A'
        REJECTED = 'R'

        Choices = (
            (PENDING, 'Pending'),
            (ACCEPTED, 'Accepted'),
            (REJECTED, 'Rejected')
        )

    requestor = models.ForeignKey(User,on_delete=CASCADE,related_name="send_requests")
    requestee = models.ForeignKey(User,on_delete=CASCADE,related_name="received_requests")
    status = models.CharField(choices=Status.Choices, max_length=1,default=Status.PENDING)

    def __str__(self):
        request_statement = "{} has sent {} a friend request, Status is {}."
        return request_statement.format(self.requestor,self.requestee,self.status)
        