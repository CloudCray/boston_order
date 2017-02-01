import datetime
from getpass import getpass
from boston_order_ivr import create_app, db
app = create_app("development")

with app.app_context():
    from boston_order_ivr.auth.models import Role, User
    user_name = input("Admin User email > ")
    user_pwd = getpass("Admin User password > ")
    user = User()
    user.email = user_name
    user.password = user_pwd
    user.active = True
    user.confirmed_at = datetime.datetime.now()
    role = Role.query.filter_by(name="Administrator").first()
    user.roles.append(role)
    role2 = Role.query.filter_by(name="User").first()
    user.roles.append(role2)
    db.session.commit()
