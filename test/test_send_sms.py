from boston_order_ivr import create_app, twilio_rest

app = create_app('development')

with app.app_context():
    # Extensions like Flask-SQLAlchemy now know what the "current" app
    # is while within this block. Therefore, you can now run........
    SMS_TO_NUMBER = "+1" + input("Your phone number (10 digits): ")
    message = twilio_rest.client.messages.create(to=SMS_TO_NUMBER,
                                          from_=twilio_rest.sms_number,
                                          body="Hello there!"
                                          )
