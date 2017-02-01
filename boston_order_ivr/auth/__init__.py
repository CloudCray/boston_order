from flask import Blueprint

bp_auth = Blueprint('auth', __name__)

from . import views
from .models import User
from .. import login


@login.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()
