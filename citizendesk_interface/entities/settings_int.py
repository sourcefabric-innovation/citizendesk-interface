entity = {
    'schema': {
        'key': {
            'type': 'string',
            'required': True,
            'unique': True
        },
        'value': {
            'type': 'integer',
            'required': True
        }
    },
    'resource_methods': ['GET', 'POST'],
    'item_methods': ['GET', 'PUT', 'PATCH']
}
