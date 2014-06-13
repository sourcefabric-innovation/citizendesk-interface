schema = {
    'query': {
        'type': 'dict',
    },
    'description': {
        'type': 'string',
    }
}
entity = {
    'schema': schema,
    'resource_methods': ['GET', 'POST'],
    'item_methods': ['GET', 'DELETE'],
    'pagination': False
}
