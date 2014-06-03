schema = {
    'authors': {'type': 'list'},
    'channels': {'type': 'list'},
    'steps': {'type': 'list'},
    'original': {'type': 'dict'},
    'produced': {'type': 'datetime'},
    'texts': {'type': 'list'},
    'verified': {'type':'boolean'}
}
entity = {
    'schema': schema,
    'resource_methods': ['GET'],
    'item_methods': ['GET', 'PUT', 'PATCH']
}
