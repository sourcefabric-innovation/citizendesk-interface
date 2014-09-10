schema = {
    'query': {
        'type': 'dict',
    },
    'description': {
        'type': 'string',
    },
    'creator': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'users',
            'field': '_id',
            'embeddable': True
        }
    }
}
entity = {
    'schema': schema,
    'resource_methods': ['GET', 'POST'],
    'item_methods': ['GET', 'DELETE'],
    'pagination': False
}
