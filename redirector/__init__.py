import logging
import os

from flask import Flask, redirect


app = Flask(__name__)
app.config['TARGET_URL'] = os.getenv('TARGET_URL')
logging.basicConfig(level=logging.INFO)


@app.route('/', defaults={'u_path': ''})
@app.route('/<path:u_path>')
# handles generic redirects for all requests that don't match a more specific
# pattern
def generic_redirect(u_path):
    url = app.config['TARGET_URL']
    return redirect(url, code=308)


@ app.route('/item/<string:aleph_id>')
# handles aleph permalink syntax http://library.mit.edu/item/001264079
def redirect_with_bibid(aleph_id):
    url = app.config['TARGET_URL']
    return redirect(f'{url}?aleph_id={aleph_id}', code=308)


@ app.route('/ping')
def ping():
    return 'pong'
