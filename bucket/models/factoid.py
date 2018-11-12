from sqlalchemy import Column, Integer, String, Boolean
from bucket.models import Base


class Factoid(Base):
    __tablename__ = 'bucket_facts'

    id = Column(Integer, primary_key=True)
    fact = Column(String)
    tidbit = Column(String)
    verb = Column(String)
    RE = Column(Boolean)
    protected = Column(Boolean)
    mood = Column(String)
    chance = Column(Integer)
