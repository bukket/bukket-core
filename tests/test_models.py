from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pytest


from bucket.models import Factoid, Base


@pytest.fixture(scope="module")
def db_setup(request):
    engine = create_engine('sqlite:///:memory:')
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    f = Factoid(
        fact='a test trigger',
        tidbit='helloooo',
        verb='is',
        RE=False,
        protected=False,
        mood='',
        chance=1)
    session.add(f)
    session.commit()

    def fin():
        Base.metadata.drop_all()

    return session


def test_factoid_query(db_setup):
    session = db_setup
    result = session.query(Factoid).first()
    result.fact == 'a test trigger'