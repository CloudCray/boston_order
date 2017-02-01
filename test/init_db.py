from boston_order_ivr import create_app, db

app = create_app('development')

Base = db.Model


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import boston_order_ivr.base.models
    import boston_order_ivr.auth.models
    Base.metadata.create_all(bind=db.engine)

with app.app_context():
    # Extensions like Flask-SQLAlchemy now know what the "current" app
    # is while within this block. Therefore, you can now run........
    init_db()
