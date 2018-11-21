import pytest
import os
from bucket.db import get_db
from bucket.models import Factoid, Base
from bucket import create_app


def test_factoid_detail(test_client):
    response = test_client.get('/factoid/1')
    assert response.status_code == 200


def test_factoid_search(test_client):
    response = test_client.get('/factoid/search/test')
    assert response.status_code == 200


def test_factoid_search_spaces(test_client):
    response = test_client.get('/factoid/search/a%20test%20trigger')
    assert response.status_code == 200


def test_search_factoid_tidbit(test_client):
    response = test_client.get('/factoid/search/hello?tidbit=true')
    assert response.status_code == 200
    assert response.json['data'][0]['id'] == 1


def test_search_factoid_tidbit_fail(test_client):
    response = test_client.get('/factoid/search/test?tidbit=true')
    assert response.status_code == 200
    assert len(response.json['data']) == 0


def test_list_exact_factoids(test_client):
    response = test_client.get('/factoid/a%20test%20trigger')
    assert response.status_code == 200
    assert response.json['data'][0]['id'] == 1


def test_root_url(test_client):
    response = test_client.get('/factoid/')
    assert response.status_code == 501


def test_factoid_search_fail(test_client):
    response = test_client.get('/factoid/search/abc123')
    assert response.status_code == 200
    assert response.json['data'] == []


def test_factoid_detail_fail(test_client):
    response = test_client.get('/factoid/2')
    assert response.status_code == 404
