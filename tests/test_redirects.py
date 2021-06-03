from flask import request
import pytest
import redirector


@pytest.fixture
def client():
    redirector.app.config['DEBUG'] = True
    redirector.app.config['TESTING'] = True
    redirector.app.config['TARGET_URL'] = 'http://example.com/hallo/'
    redirector.app.config['ALMA_SRU'] = 'https://mit.alma.exlibrisgroup.com/view/sru/01MIT_INST?version=1.2&operation=searchRetrieve&recordSchema=dc&query=alma.all_for_ui='
    redirector.app.config['PRIMO_URL'] = 'http://example.com/primo/'

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
