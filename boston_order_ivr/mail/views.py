from flask_rq import job
from .models import EmailMessage


@job
def send_email(subscriber, subject, message):
    email_message = EmailMessage(
        subject=subject,
        recipients=[subscriber.email_address]
    )
    email_message.body = message
    email_message.send()