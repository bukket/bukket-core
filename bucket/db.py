import logging

from flask import current_app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from bucket.models import Base


def setup_session(host=None, user=None, password=None, port=5432, proto='postgresql://', db='bucket'):
    logging.info("Setting up database.")
    if proto.startswith('postgresql'):
        engine = create_engine(f"{proto}{user}:{password}@{host}:{port}/{db}")
    elif proto.startswith('sqlite'):
        # engine = create_engine(f"sqlite:///:memory:", echo="debug")
        engine = create_engine(f"sqlite:///:memory:")
    Session = sessionmaker(bind=engine)
    logging.info("Setup db sessionmaker.")
    session = Session()

    # We have set the schema=bucket in declarative_base (bucket.models.Base), but this doesn't work for
    # sqlite3 in-memory databases, so we have to do this workaround. Ideally, we could do this in a
    # pre-init hook or something like that, but I'm too lazy to implement that.
    if proto.startswith('sqlite'):
        session.execute("ATTACH DATABASE ':memory:' as bucket;")
    Base.metadata.create_all(engine)
    session.close()
    logging.info("DB metadata created.")
    return Session


def get_db():
    if hasattr(current_app, 'db'):
        logging.debug("'db' not in current_app, setting up session.")
        current_app.db = setup_session(**current_app.config['DATABASE'])

    return current_app.db


class connection(object):

    def __enter__(self):
        logging.debug("Starting db session.")
        Session = current_app.db
        self.session = Session()
        return self.session

    def __exit__(self, *exc):
        try:
            logging.debug("Flushing session")
            self.session.commit()
        except Exception as e:
            logging.warn("An exception occurred when attempting to commit.")
            logging.warn(e)
            self.session.rollback()
            raise
        finally:
            logging.debug("Closing db session.")
            self.session.close()
