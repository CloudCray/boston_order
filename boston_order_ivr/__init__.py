from flask import Flask
from .config import read_config

app = Flask(__name__)


def create_app(config_name):
    app = Flask(__name__)

    flask_config = read_config("flask", config_name)

    app.config.update(
        ENVIRONMENT_NAME=config_name,
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        DEBUG=flask_config["debug"],
        SECRET_KEY=flask_config["secret_key"],
    )

    from .views import bp_ivr
    app.register_blueprint(bp_ivr)

    app.jinja_env.globals['get_resource_as_string'] = get_resource_as_string
    return app


def get_resource_as_string(name, charset='utf-8'):
    with app.open_resource(name) as f:
        return f.read().decode(charset)
