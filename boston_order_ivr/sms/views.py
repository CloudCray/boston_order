from flask_rq import job
from .. import twilio_rest, rq
import time


@job
def send_text(subscriber, message):
    twilio_rest.client.messages.create(
        to=subscriber.sms_number,
        from_=twilio_rest.sms_number,
        body=message
    )

