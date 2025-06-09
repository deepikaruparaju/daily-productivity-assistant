from plyer import notification

def notify_user(title, message):
    notification.notify(title=title, message=message, timeout=5)