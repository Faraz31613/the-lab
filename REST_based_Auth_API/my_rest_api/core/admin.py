from django.contrib import admin

from .models import Comment, Friend, Like, Message, Notification, Post, Request

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Request)
admin.site.register(Notification)
admin.site.register(Like)
admin.site.register(Message)
admin.site.register(Friend)
