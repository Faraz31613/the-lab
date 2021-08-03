from .models import Notification


def create_notification(
    request,
    to_user,
    notification,
    notification_source_type,
    user_by,
    notification_source_id,
):
    notification = Notification.objects.create(
        user=to_user,
        notification=notification,
        user_by=user_by,
        notification_source_id=notification_source_id,
        notification_source_type=notification_source_type,
    )
