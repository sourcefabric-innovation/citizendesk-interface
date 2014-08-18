entity = {
    'schema': {
        'name': {
            'type': 'string',
        },
        'description': {
            'type': 'string',
        },
        'variation': {
            'type': 'string',
            'allowed': [
                'label-default',
                'label-primary',
                'label-success',
                'label-info',
                'label-warning',
                'label-danger',
            ]
        },
    },
    'resource_methods': ['GET', 'POST'],
    'item_methods': ['GET', 'PUT', 'DELETE', 'PATCH'],
    'pagination': False,
}
