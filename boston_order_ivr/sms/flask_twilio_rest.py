from twilio.rest import TwilioRestClient


class TwilioRest(TwilioRestClient):

    def __init__(self, app=None):
        self.app = app
        self.sms_number = None
        if app is not None:
            self.client = self.init_app(app)
        else:
            self.client = None

    def init_twilio(self, config):
        return TwilioRestClient(
            config.get("TWILIO_ACCOUNT_SID"),
            config.get("TWILIO_AUTH_TOKEN"),
        )

    def init_app(self, app):
        self.client = self.init_twilio(app.config)
        self.sms_number = app.config.get("TWILIO_SMS_NUMBER")
        app.extensions = getattr(app, 'extensions', {})
        app.extensions['twilio'] = self.client
        return self.client

    def __getattr__(self, name):
        return getattr(self.client, name, None)
