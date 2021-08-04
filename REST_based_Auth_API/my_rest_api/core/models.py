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
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=300)

    def __str__(self):
        return self.comment


class Request(models.Model):
    class Status:
        PENDING = "P"
        ACCEPTED = "A"
        REJECTED = "R"

        Choices = ((PENDING, "Pending"), (ACCEPTED, "Accepted"), (REJECTED, "Rejected"))

    requestor = models.ForeignKey(User, on_delete=CASCADE, related_name="send_requests")
    requestee = models.ForeignKey(
        User, on_delete=CASCADE, related_name="received_requests"
    )
    status = models.CharField(
        choices=Status.Choices, max_length=1, default=Status.PENDING
    )

    def __str__(self):
        request_statement = "{} has sent {} a friend request, Status is {}."
        return request_statement.format(self.requestor, self.requestee, self.status)


class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, related_name="user")
    friend = models.ForeignKey(User, on_delete=CASCADE, related_name="friend")
    status = models.CharField(max_length=10, default="Friends")


class Notification(models.Model):
    class NotificationType:
        REQUEST = "R"
        LIKE = "L"
        COMMENT = "C"
        REPLY = "RC"
        MESSAGE = "M"

        notification_type = (
            (REQUEST, "Request"),
            (LIKE, "Like"),
            (COMMENT, "Comment"),
            (REPLY, "Reply"),
            (MESSAGE, "Message"),
        )

    user = models.ForeignKey(
        User, on_delete=CASCADE, related_name="notification_sent_to_user"
    )
    notification = models.CharField(max_length=50)
    is_read = models.BooleanField(default=False)
    user_by = models.IntegerField(null=True)
    notification_source_id = models.IntegerField(null=True)  # id of comment,post etc.
    notification_source_type = models.CharField(
        choices=NotificationType.notification_type, max_length=2
    )

    def __str__(self):
        return self.notification
