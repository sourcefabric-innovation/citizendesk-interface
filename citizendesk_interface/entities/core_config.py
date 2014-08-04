entity = {
    'schema': {
        'type': {
            'type': 'string',
            'required': True,
            'unique': True
        },
        'set': {
            'type': 'dict'
        }
    },
    # no `POST` nor `DELETE`, just update configuration defaults in
    # the database
    'resource_methods': ['GET'],
    'item_methods': ['GET', 'PUT', 'PATCH'],
    'pagination': False,
}
