import pytest
import redirector


@pytest.fixture
def client():
    redirector.app.config['TESTING'] = True
    redirector.app.config['TARGET_URL'] = 'http://example.com/hallo/'

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


def test_redirect_with_permalink_pattern(client):
    response = client.get('/item/123')
    url = 'http://example.com/hallo/?aleph_id=123'
    assert url in response.location
