from .functions import mask

entity = {
    'schema': {
        'spec': {
            'type': 'dict',
            'schema': {
                'consumer_secret': { 'type': 'string'},
                'access_token_key': { 'type': 'string'},
                'consumer_key': { 'type': 'string'},
                'access_token_secret': { 'type': 'string'}
            }
        },
        'user_id': { 'type':'objectid' }
    },
    'resource_methods': ['GET', 'POST'],
    'item_methods': ['GET', 'DELETE'],
    'pagination': False,
}

def before_returning_twt_oauths(response):
    for item in response['_items']:
        for attribute in [
                'consumer_secret',
                'access_token_key',
                'consumer_key',
                'access_token_secret'
        ]:
            item['spec'][attribute] = mask(item['spec'][attribute])

def init(app):
    app.on_fetched_resource_twt_oauths += before_returning_twt_oauths
