from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text_post = models.CharField(max_length=500)

    def __str__(self):
        return self.text_post


class Comment(models.Model):
    class CommentType:
        POST = "P"  # comment on post
        COMMENT = "C"  # comment on comment:reply

        comment_type = (
            (POST, "Comment"),
            (COMMENT, "Reply"),
        )

    user = models.ForeignKey(
        User, on_delete=CASCADE, related_name="commentor", null=True
    )
    post = models.ForeignKey(
        Post, on_delete=CASCADE, related_name="commented_on_post", null=True
    )
    comment = models.ForeignKey(
        "self", on_delete=models.CASCADE, related_name="parent_comment", null=True
    )
    comment_text = models.CharField(max_length=300)

    def __str__(self):
        return self.comment_text


class Request(models.Model):
    class Status:
        PENDING = "P"
        ACCEPTED = "A"
        REJECTED = "R"

        Choices = ((PENDING, "Pending"), (ACCEPTED, "Accepted"),
                   (REJECTED, "Rejected"))

    requestor = models.ForeignKey(
        User, on_delete=CASCADE, related_name="send_requests")
    requestee = models.ForeignKey(
        User, on_delete=CASCADE, related_name="received_requests"
    )
    status = models.CharField(
        choices=Status.Choices, max_length=1, default=Status.PENDING
    )

    def __str__(self):
        request_statement = f"{self.requestor} has sent {self.requestee} a friend request, Status is {self.status}."
        return request_statement


class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, related_name="user")
    friend = models.ForeignKey(User, on_delete=CASCADE, related_name="friend")
    request = models.ForeignKey(
        Request, on_delete=CASCADE, related_name="friend_request", null=True
    )
    status = models.CharField(max_length=10, default="Friends")

    def __str__(self):
        return f"{self.user}'s friend is {self.friend}"


class Notification(models.Model):
    class NotificationType:
        REQUEST = "R"
        LIKE = "L"
        COMMENT = "C"
        MESSAGE = "M"

        notification_type = (
            (REQUEST, "Request"),
            (LIKE, "Like"),
            (COMMENT, "Reply"),
            (MESSAGE, "Message"),
        )

    user = models.ForeignKey(
        User, on_delete=CASCADE, related_name="notification_sent_to_user"
    )
    notification = models.CharField(max_length=50)
    is_read = models.BooleanField(default=False)
    user_by = models.ForeignKey(User, on_delete=CASCADE, null=True)
    post = models.ForeignKey(
        Post, on_delete=CASCADE, related_name="post_notification", null=True
    )
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        related_name="comment_notification",
        null=True,
    )
    notification_source_type = models.CharField(
        choices=NotificationType.notification_type, max_length=1
    )

    def __str__(self):
        return self.notification


class Like(models.Model):
    class LikeType:
        POST = "P"  # liked a post
        COMMENT = "C"  # Liked comment:reply

        like_type = (
            (POST, "Post"),
            (COMMENT, "Comment"),
        )

    user = models.ForeignKey(User, on_delete=CASCADE,
                             related_name="liker", null=True)
    post = models.ForeignKey(
        Post, on_delete=CASCADE, related_name="liked_post", null=True
    )
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name="liked_comment", null=True
    )
    is_like = models.BooleanField(default=False)

    def __str__(self):
        post_or_comment = "Post" if self.comment==None else "Comment"
        likes_or_unliked = "Liked" if self.is_like== True else "Unliked"
        return f"{post_or_comment} is {likes_or_unliked}"


class Message(models.Model):
    sender = models.ForeignKey(
        User, on_delete=CASCADE, related_name="message_sender")
    receiver = models.ForeignKey(
        User, on_delete=CASCADE, related_name="message_receiver"
    )
    message = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.sender.username} | {self.message} | {self.receiver.username}"
