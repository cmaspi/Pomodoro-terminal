from plyer import notification


def notify(title, message, app_name):
    notification.notify(
        title=title,
        message=message,
        app_name=app_name,
    )


def sound():
    print('\007')
