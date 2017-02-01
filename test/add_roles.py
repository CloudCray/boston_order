from boston_order_ivr import create_app, db

app = create_app('development')

Base = db.Model

with app.app_context():
    # Extensions like Flask-SQLAlchemy now know what the "current" app
    # is while within this block. Therefore, you can now run........
    import boston_order_ivr.auth.models as models
    models.Role.insert_roles()
