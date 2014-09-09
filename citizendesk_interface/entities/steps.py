entity = {
    'schema': {
        'description': {
            'type': 'string',
            'required': True
        },
        'mandatory': {
            'type': 'boolean',
            'required': True
        }
    },
    'resource_methods': ['GET', 'POST'],
    'item_methods': ['GET', 'PUT', 'PATCH', 'DELETE'],
    'pagination': False
}
