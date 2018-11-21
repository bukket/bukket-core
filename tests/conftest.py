import os

import pytest

from bucket.models import Factoid, Base
from bucket.db import get_db
from bucket import create_app

@pytest.fixture(scope="session")
def test_app(request):
    app = create_app(test_config={
        'TESTING': True, 
        'DATABASE': {
            'proto': 'sqlite:///',
        }})

    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app


@pytest.fixture(scope="session")
def db_setup(test_app):
    session = get_db()
    f = Factoid(
        fact='a test trigger',
        tidbit='helloooo',
        verb='is',
        re=False,
        protected=False,
        mood=0,
        chance=1)
    session.add(f)
    session.commit()

@pytest.fixture(scope="session")
def test_client(test_app, db_setup):
    return test_app.test_client()
