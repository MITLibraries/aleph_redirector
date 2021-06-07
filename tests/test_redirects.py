import os
import pytest
import redirector


@pytest.fixture
def client():
    os.environ['FLASK_ENV'] = 'testing'
    with redirector.app.test_client() as client:
        yield client


def test_ping(client):
    rv = client.get('/ping')
    assert b'pong' in rv.data


def test_redirect_with_no_args(client):
    response = client.get('/')
    url = 'http://example.com/hallo/'
    assert url in response.location


def test_redirect_with_non_permalink_pattern(client):
    response = client.get('/i/am/a/non/handled/path')
    url = 'http://example.com/hallo/'
    assert url in response.location


@pytest.mark.vcr
def test_redirect_with_permalink_pattern(client):
    response = client.get('/item/000095961')
    expected = 'http://example.com/primo/alma990000959610206761'
    assert response.headers['location'] == expected


@pytest.mark.vcr
def test_redirect_to_generic_with_permalink_pattern_no_match(client):
    response = client.get('/item/asdfasdfasfasdfasdfasdf')
    expected = 'http://example.com/hallo/'
    assert response.headers['location'] == expected
