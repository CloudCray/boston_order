from flask import Blueprint
bp_ivr = Blueprint('ivr', __name__, url_prefix="/ivr")

from . import views