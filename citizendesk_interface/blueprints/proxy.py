"""
This is a blueprint for proxying requests to `citizendesk-core`. Most
of the controllers here should just wrap a call to the core, in order
to avoid clients the complexity of dealing with different servers
"""
from flask import Blueprint, make_response
import requests
from raven import Client

client = Client('http://b1901abf077d476ba253bce45dd5bf91:cf99fe3dade94a599e9a79aada3f6266@sentry.sourcefabric.org/8')
core      = 'http://localhost:9060'
blueprint = Blueprint('proxy', __name__)

def start_stop(id, action):
    location = core + '/feeds/twt/stream/{0}/{1}'.format(id, action)
    try:
        r = requests.post(location)
        r.raise_for_status()
        return make_response(r.text, r.status_code)
    except requests.exceptions.HTTPError as error:
        client.captureException()
        return error.code

@blueprint.route('/start-stream/<id>')
def monitor_start(id):
    return start_stop(id, 'start')

@blueprint.route('/stop-stream/<id>')
def monitor_stop(id):
    return start_stop(id, 'stop')
