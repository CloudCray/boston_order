from sqlalchemy import Column, Integer, String, Text, ForeignKey
from .. import db


Base = db.Model


class IVRCallNode(Base):
    __tablename__ = "ivr_call_node"
    id = Column(Integer, primary_key=True)
    name = Column(String(length=255))
    node_type = Column(String(length=50))
    spoken_text = Column(Text)
    mp3_file = Column(Integer, ForeignKey(""))


class MenuNodeOption(IVRCallNode):
    keystroke = Column(String(length=10))
    redirect_node = Column(Integer, ForeignKey("ivr_call_node.id"))


class CallRecording(Base):
    __tablename__ = "mp3_file"
    id = Column(Integer, primary_key=True)
    name = Column(String(length=500))
    location = Column(String(length=500))
