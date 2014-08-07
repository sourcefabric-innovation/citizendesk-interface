# see also https://github.com/sourcefabric-innovation/citizendesk-core/blob/master/src/citizendesk/feeds/any/coverage/storage.py#L18
entity = {
    'schema': {
        'title': {
            'type': 'string',
            'required': True
        },
        'description': {'type': 'string'},
        'active': {'type': 'boolean'},
    },
    'resource_methods': ['GET', 'POST'],
    'item_methods': ['GET', 'PUT', 'DELETE', 'PATCH'],
    'pagination': False,
}
