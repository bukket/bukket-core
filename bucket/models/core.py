from sqlalchemy import Column, BigInteger,  String, Boolean, SmallInteger, DateTime
from sqlalchemy.types import Enum
from sqlalchemy.ext.compiler import compiles
from bucket.models.base import Base
from bucket.models.enums import BucketVarsPerms, BucketVarsType, GendersGender


# sqlite does not do auto-increment on anything but Integer types, hence this code
# I took this code from here:
# https://docs.sqlalchemy.org/en/latest/dialects/sqlite.html#allowing-autoincrement-behavior-sqlalchemy-types-other-than-integer-integer
class SLBigInteger(BigInteger):
    pass


@compiles(SLBigInteger, 'sqlite')
def bi_c(element, compiler, **kw):
    return 'INTEGER'


class Factoid(Base):
    __tablename__ = 'bucket_facts'

    id = Column(SLBigInteger, primary_key=True)
    fact = Column(String, nullable=False)
    tidbit = Column(String, nullable=False)
    verb = Column(String(16), default='is', nullable=False)
    re = Column(Boolean, default=False, nullable=False)
    protected = Column(Boolean, nullable=False)
    mood = Column(SmallInteger)
    chance = Column(SmallInteger)

    def serialize(self):
        return {
            'id': self.id,
            'fact': self.fact,
            'tidbit': self.tidbit,
            'verb': self.verb,
            're': self.re,
            'protected': self.protected,
            'mood': self.mood,
            'chance': self.chance
        }


class Items(Base):
    __tablename__ = 'bucket_items'

    id = Column(SLBigInteger, primary_key=True)
    channel = Column(String(64), nullable=False)
    what = Column(String(255), nullable=False)
    user = Column(String(64), nullable=False)


class Values(Base):
    __tablename__ = 'bucket_values'

    id = Column(SLBigInteger, primary_key=True)
    var_id = Column(BigInteger, nullable=False)
    value = Column(String(32), nullable=False)


class Vars(Base):
    __tablename__ = 'bucket_vars'

    id = Column(SLBigInteger, primary_key=True)
    name = Column(String(16), nullable=False)
    perms = Column(Enum(BucketVarsPerms), default=BucketVarsPerms['read-only'], nullable=False)
    type = Column(Enum(BucketVarsType), default=BucketVarsType.var, nullable=False)


class Genders(Base):
    __tablename__ = 'genders'

    id = Column(SLBigInteger, primary_key=True)
    nick = Column(String(30), nullable=False)
    gender = Column(Enum(GendersGender), default=GendersGender.Androgynous, nullable=False)
    stamp = Column(DateTime(timezone=True), nullable=False)


class Mainlog(Base):
    __tablename__ = 'mainlog'

    id = Column(SLBigInteger, primary_key=True)
    stamp = Column(DateTime(timezone=True), nullable=False)
    msg = Column(String(512), nullable=False)


class Word2Id(Base):
    __tablename__ = 'word2id'

    id = Column(SLBigInteger, primary_key=True)
    word = Column(String(32), nullable=False)
    lines = Column(BigInteger, nullable=False)


class Word2Line(Base):
    __tablename__ = 'word2line'

    # TODO: Do these need to be foreign key constraints?
    id = Column(SLBigInteger, primary_key=True)
    word = Column(SLBigInteger)
    line = Column(SLBigInteger)
