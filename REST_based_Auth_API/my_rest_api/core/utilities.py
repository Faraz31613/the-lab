from .models import Notification

def create_notification(request,to_user,notification):
    notification = Notification.objects.create(user = to_user,notification = notification)