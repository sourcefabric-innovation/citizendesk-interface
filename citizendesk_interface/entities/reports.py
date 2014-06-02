schema = {
    'authors': {'type': 'list'},
    'channels': {'type': 'list',},
    'original': {'type': 'dict'},
    'produced': {'type': 'datetime'},
    'texts': {'type': 'list'},
}
entity = {
    'schema': schema,
    'resource_methods': ['GET'],
    'item_methods': ['GET', 'PUT', 'PATCH']
}
