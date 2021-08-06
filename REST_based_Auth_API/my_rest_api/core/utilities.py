from .models import Friend, Notification


def create_notification(
    request,
    to_user,
    notification,
    notification_source_type,
    user_by,
    post,
    comment,
):
    Notification.objects.create(
        user=to_user,
        notification=notification,
        user_by=user_by,
        post=post,
        comment=comment,
        notification_source_type=notification_source_type,
    )


def save_friend(request, user, friend, friend_request):
    Friend.objects.create(user=user, friend=friend, request=friend_request)
