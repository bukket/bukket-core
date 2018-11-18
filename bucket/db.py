from flask import current_app, g
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from bucket.models import Base


def setup_session(host=None, user=None, password=None, port=5432, proto='postgresql://', db='bucket'):
    engine = create_engine(f"{proto}{user}:{password}@{host}:{port}/{db}")
    Session = sessionmaker(bind=engine)
    session = Session()
    # Required for postgres for now, until we figure out how to get the schema set correctly
    # via sqlalchemy, which helpfully leaves this as an exercise for the reader.
    session.execute('SET search_path TO bucket')
    Base.metadata.create_all(engine)
    return session


def get_db():
    if 'db' not in g:
        g.db = setup_session(**current_app.config['DATABASE'])

    return g.db
