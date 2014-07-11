schema = {
    'authors': {'type': 'list'},
    'channels': {'type': 'list'},
    'steps': {'type': 'list'},
    'assignments': {'type': 'list'},
    'original': {'type': 'dict'},
    'produced': {
        'type': 'datetime',
        'required': True
    },
    'texts': {'type': 'list'},
    'verified': {'type':'boolean'},
    'feed_type': {'type':'string'},
    'session': {'type':'string'},
    'local': {'type':'boolean'},
    # according to Martin, this is where the user id is specified, but
    # just when `local` is true (citizendesk users)
    'user_id': {
        'type':'objectid',
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
    'item_methods': ['GET', 'PUT', 'PATCH']
}
