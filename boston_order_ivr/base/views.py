from flask import render_template
from . import bp_base
from .models import LandingUpdate

from ..auth.views import AdminModelView
from .. import admin, db


@bp_base.route("/")
def index():
    lus = LandingUpdate.query.filter_by(active=True).all()
    return render_template("base/index.html", landing_updates=lus)


class LandingUpdateAdminView(AdminModelView):

    def on_model_change(self, form, instance, is_created):
        instance.on_model_updated(is_created)

admin.add_view(LandingUpdateAdminView(LandingUpdate, db.session))
