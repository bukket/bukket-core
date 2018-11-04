import pytest
from bucket import create_app


@pytest.fixture
def app():
    app = create_app({'TESTING': True})
    yield app


@pytest.fixture
def client(app):
    return app.test_client()


def test_root_url(client):
    response = client.get('/')
    assert response.status_code == 200
