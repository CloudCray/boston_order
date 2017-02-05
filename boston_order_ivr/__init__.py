from flask import Flask
from .config import read_config

from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_admin import Admin
from flaskext.markdown import Markdown
from flask_rq import RQ

from boston_order_ivr.sms.flask_twilio_rest import TwilioRest

app = Flask(__name__)

login = LoginManager()
login.session_protection = 'strong'
login.login_view = 'auth.login'

admin = Admin(template_mode='bootstrap3')
db = SQLAlchemy()
mail = Mail()
rq = RQ()

twilio_rest = TwilioRest()


def create_app(config_name):
    app = Flask(__name__)

    db_config = read_config("database", config_name)
    flask_config = read_config("flask", config_name)
    email_config = read_config("mail", config_name)
    twilio_config = read_config("twilio", config_name)
    rq_config = read_config("redis", config_name)

    db_driver = db_config["driver"]
    if db_driver == "sqlite":
        db_uri = '{0}:///./../{1}'.format(
                db_config["driver"],
                db_config["database"]
                )
    else:
        db_uri = '{0}://{1}:{2}@{3}/{4}'.format(
                db_config["driver"],
                db_config["user"],
                db_config["password"],
                db_config["server"],
                db_config["database"])

    app.config.update(
        ENVIRONMENT_NAME=config_name,
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        DEBUG=flask_config["debug"],
        SECRET_KEY=flask_config["secret_key"],
        SQLALCHEMY_DATABASE_URI=db_uri,
        MAIL_SERVER=email_config["server"],
        MAIL_USERNAME=email_config["username"],
        MAIL_PASSWORD=email_config["password"],
        MAIL_PREFIX=email_config["prefix"],
        MAIL_SENDER=email_config["sender"],
        TWILIO_ACCOUNT_SID=twilio_config["account_sid"],
        TWILIO_AUTH_TOKEN=twilio_config["auth_token"],
        TWILIO_SMS_NUMBER=twilio_config["sms_number"],
        RQ_OTHER_HOST=rq_config["host"],
        RQ_OTHER_PORT=rq_config["port"],
        RQ_OTHER_PASSWORD=rq_config["password"],
        RQ_OTHER_DB=rq_config["db"],
    )

    db.init_app(app)
    login.init_app(app)
    mail.init_app(app)
    admin.init_app(app)
    Markdown(app)
    rq.init_app(app)

    twilio_rest.init_app(app)

    from .base import bp_base
    from .auth import bp_auth
    from .ivr import bp_ivr

    app.register_blueprint(bp_base)
    app.register_blueprint(bp_auth)
    app.register_blueprint(bp_ivr)

    app.jinja_env.globals['get_resource_as_string'] = get_resource_as_string
    return app


def get_resource_as_string(name, charset='utf-8'):
    with app.open_resource(name) as f:
        return f.read().decode(charset)
