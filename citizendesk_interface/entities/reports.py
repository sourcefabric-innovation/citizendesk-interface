schema = {
    'authors': {'type': 'list'},
    'channels': {'type': 'list'},
    'steps': {'type': 'list'},
    'original': {'type': 'dict'},
    'produced': {
        'type': 'datetime',
        'required': True
    },
    'texts': {'type': 'list'},
    'verified': {'type':'boolean'}
}
entity = {
    'schema': schema,
    'resource_methods': ['GET', 'POST'],
    'item_methods': ['GET', 'PUT', 'PATCH']
}
