from django.contrib import admin

from .models import Comment, Notification, Post, Request

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Request)
admin.site.register(Notification)
