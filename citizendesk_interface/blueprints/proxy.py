"""
This is a blueprint for proxying requests to `citizendesk-core`. Most
of the controllers here should just wrap a call to the core, in order
to avoid clients the complexity of dealing with different servers
"""
import json

from flask import Blueprint, make_response, request
import requests
from raven import Client
from flask_cors import cross_origin

client    = Client('http://b1901abf077d476ba253bce45dd5bf91:cf99fe3dade94a599e9a79aada3f6266@sentry.sourcefabric.org/8')
core      = 'http://localhost:9060'
blueprint = Blueprint('proxy', __name__)

def post_core(url, data={}):
    serialised = json.dumps(data)
    headers    = { 'content-type': 'application/json' }
    try:
        r = requests.post(url, data=serialised, headers=headers)
        r.raise_for_status()
        return make_response(r.text, r.status_code)
    except requests.exceptions.HTTPError as error:
        client.captureException(data={
                'extra': {
                    'url': url,
                    'payload': serialised
                }
        })
        text = 'Error while communicating with citizendesk-core: {}\n'.format(r.status_code)
        return make_response(text, 500)

def start_stop(id, action):
    location = core + '/feeds/twt/stream/{0}/{1}'.format(id, action)
    return post_core(location)

@blueprint.route('/start-stream/<id>')
@cross_origin(headers=['Content-Type,Authorization'])
def monitor_start(id):
    return start_stop(id, 'start')

@blueprint.route('/stop-stream/<id>')
@cross_origin(headers=['Content-Type,Authorization'])
def monitor_stop(id):
    return start_stop(id, 'stop')

@blueprint.route('/start-twitter-search/', methods=['POST'])
@cross_origin(headers=['Content-Type,Authorization'])
def start_search():
    return post_core(core + '/feeds/twt/search/', data=request.get_json())

@blueprint.route('/fetch-citizen-alias/', methods=['POST'])
@cross_origin(headers=['Content-Type,Authorization'])
def fun():
    data = request.get_json()
    auth = data['authority']
    name = data['name']
    # more authorities could be eventually added
    map = {
        'twitter': '/feeds/twt/citizen/alias/name/{0}/request/',
    }
    url = core + map[auth].format(name)
    return post_core(url)

@blueprint.route('/mobile-reply/', methods=['POST'])
@cross_origin(headers=['Content-Type,Authorization'])
def reply():
    return post_core(core + '/feeds/sms/reply/', data=request.get_json())

@blueprint.route('/publish/', methods=['POST'])
@cross_origin(headers=['Content-Type,Authorization'])
def publish():
    data = request.get_json();
    location = core + '/feeds/any/report/id/{0}/publish/{1}/'.format(
        data['report'],
        data['coverage']
    )
    return post_core(location)

@blueprint.route('/unpublish/', methods=['POST'])
@cross_origin(headers=['Content-Type,Authorization'])
def unpublish():
    data = request.get_json();
    location = core + '/feeds/any/report/id/{0}/unpublish/{1}/'.format(
        data['report'],
        data['coverage']
    )
    return post_core(location)
