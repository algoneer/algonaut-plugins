from algonaut.settings import settings
from algonaut.utils.email import send_email


def send(data):
    email = settings.get('contact-form.email')
    if not email:
        return
    send_email(to=email,
               subject='New contact form',
               text=str(data))
