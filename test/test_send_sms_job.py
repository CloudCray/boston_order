from boston_order_ivr import create_app, rq
from boston_order_ivr.sms.views import send_text
from time import sleep
from collections import namedtuple

app = create_app('development')

with app.app_context():
    # Extensions like Flask-SQLAlchemy now know what the "current" app
    # is while within this block. Therefore, you can now run........
    SMS_TO_NUMBER = "+16163040146"  # + input("Your phone number (10 digits): ")
    Subscriber = namedtuple("Subscriber", "sms_number")
    subs = Subscriber(sms_number=SMS_TO_NUMBER)
    send_text.delay(subs, "Hello, world!")
    sleep(20)
    print("Thinking about it....")
    sleep(20)

