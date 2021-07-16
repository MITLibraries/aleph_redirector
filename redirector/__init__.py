import logging
import os

import requests
import sentry_sdk

from flask import Flask, redirect

from redirector import primonator

from xml.etree.ElementTree import fromstring, ElementTree
from sentry_sdk.integrations.flask import FlaskIntegration

if os.getenv('SENTRY_DSN'):
    sentry_sdk.init(
        dsn=os.getenv('SENTRY_DSN'),
        integrations=[FlaskIntegration()],
    )

app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(primonator.bp)


flask_env = os.getenv('FLASK_ENV')

if flask_env == 'development':
    app.config.from_object('redirector.config.DevelopmentConfig')
elif flask_env == 'production':
    app.config.from_object('redirector.config.Config')
else:
    app.config.from_object('redirector.config.TestingConfig')


logging.basicConfig(level=logging.INFO)


@app.route('/', defaults={'u_path': ''})
@app.route('/<path:u_path>')
# handles generic redirects for all requests that don't match a more specific
# pattern
def generic_redirect(u_path):
    url = app.config['TARGET_URL']
    return redirect(url, code=308)


@app.route('/item/<string:aleph_id>')
# handles aleph permalink syntax http://library.mit.edu/item/001264079
def redirect_with_bibid(aleph_id):
    url, code = alma_lookup(aleph_id)
    return redirect(url, code)


@ app.route('/ping')
def ping():
    return 'pong'


def alma_lookup(aleph_id):
    # <subfield code="a">(MCM)000157165MIT01</subfield>
    # https://mit.alma.exlibrisgroup.com/view/sru/01MIT_INST?version=1.2&operation=searchRetrieve&recordSchema=marcxml&query=alma.all_for_ui=000095961MIT01
    alma_sru = app.config['ALMA_SRU'] + aleph_id + 'MIT01'
    retrieve = requests.get(alma_sru)
    url = app.config['TARGET_URL']
    code = 308

    if retrieve.status_code != 200:
        logging.info(f"Alma response code: {retrieve.status_code}")
        return url, code

    tree = ElementTree(fromstring(retrieve.content))

    root = tree.getroot()

    if 'errors' in root:
        logging.info('Errors in data returned from Alma')
        return url, code

    ns = {'x': 'http://www.loc.gov/zing/srw/'}

    # if we get exactly one record back, it's the one we want so redirct to it
    if len(tree.findall(".//x:record/x:recordIdentifier", ns)) == 1:
        url = app.config['PRIMO_URL']
        alma_id = tree.findall(".//x:record/x:recordIdentifier", ns)[0]

        return f'{url}alma{alma_id.text}', code

    return url, code


@app.route('/debug-sentry')
def trigger_error():
    division_by_zero = 1 / 0
