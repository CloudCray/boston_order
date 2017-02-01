from sqlalchemy import Column, Integer, Boolean, Text, String, DateTime
from datetime import datetime

from .. import db

Base = db.Model


class LandingUpdate(Base):
    __tablename__ = "landing_update"
    id = Column(Integer, primary_key=True)
    language = Column(String(length=50))
    label = Column(String(length=50))
    body = Column(Text)
    order = Column(Integer)
    active = Column(Boolean)
    date_updated = Column(DateTime)

    def __unicode__(self):
        return self.language

    def __repr__(self):
        return str(self.id) + ". " + self.language

    def on_model_updated(self, is_created):
        if is_created:
            self.date_updated = datetime.now()
            updates = LandingUpdate.query.all()
            if len(updates) > 1:
                ordinals = [x.order for x in updates]
                print(ordinals)
                max_ordinal = max(ordinals)
                self.order = max_ordinal + 1
            else:
                self.order = 0
        self.date_updated = datetime.now()
