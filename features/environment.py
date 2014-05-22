from citizendesk_interface import get_app

def before_all(context):
    # http://flask.pocoo.org/docs/testing/
    citizendesk = get_app({
            'MONGO_DBNAME': 'citizendesk-test'
    })
    citizendesk.config['TESTING'] = True
    context.app = citizendesk.test_client()
