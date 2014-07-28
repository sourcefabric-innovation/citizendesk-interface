entity = {
    'schema': {
        'spec': {
            'type': 'dict',
            'schema': {
                'follow': { 'type': 'list'},
                'language': { 'type': 'list'},
                'locations': { 'type': 'list'},
                'track': { 'type': 'list'}
            }
        }
    },
    'resource_methods': ['GET', 'POST'],
    'item_methods': ['GET', 'DELETE', 'PATCH'],
    'pagination': False
}
