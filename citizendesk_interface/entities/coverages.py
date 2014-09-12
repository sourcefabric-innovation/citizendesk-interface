from uuid import uuid4

# see also https://github.com/sourcefabric-innovation/citizendesk-core/blob/master/src/citizendesk/feeds/any/coverage/storage.py#L18
entity = {
    'schema': {
        'title': {
            'type': 'string',
            'required': True
        },
        'description': {'type': 'string'},
        'active': {'type': 'boolean'},
        'uuid': {
            'type': 'string',
            'required': True
        }
    },
    'resource_methods': ['GET', 'POST'],
    'item_methods': ['GET', 'PUT', 'DELETE', 'PATCH'],
    'pagination': False,
}

def on_insert_coverages(items):
    for item in items:
        item['uuid'] = str(uuid4().hex)

def init(app):
    app.on_insert_coverages += on_insert_coverages
