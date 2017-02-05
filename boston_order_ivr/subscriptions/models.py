from sqlalchemy import Column, Integer, String, Text, ForeignKey
from .. import db


Base = db.Model


class Subscriber(Base):
    __tablename__ = "subscriptions"
    id = Column(Integer, primary_key=True)
    email_address = Column(String(length=500))
    sms_number = Column(String(length=20))
    language_preference = String(length=20)
