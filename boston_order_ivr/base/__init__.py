from flask import Blueprint
bp_base = Blueprint('base', __name__)

from . import views