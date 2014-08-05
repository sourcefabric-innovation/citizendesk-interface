# references are not embeddable when they may be missing. if their
# value is null, currently (July 2014), Eve throws an error when
# trying to embed it
schema = {
    'authors': {'type': 'list'},
    'channels': {'type': 'list'},
    'steps': {'type': 'list'},
    'assignments': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': {
                'user_id': {
                    'type': 'objectid'
                }
            }
        }
    },
    'original': {'type': 'dict'},
    'produced': {
        'type': 'datetime',
        'required': True
    },
    'created': {
        'type': 'datetime',
        'required': True
    },
    'texts': {'type': 'list'},
    'verified': {'type':'boolean'},
    'summary': {'type':'boolean'},
    'proto': {'type':'boolean'},
    'feed_type': {'type':'string'},
    'session': {'type':'string'},
    'local': {'type':'boolean'},
    # according to Martin, this is where the user id is specified, but
    # just when `local` is true (citizendesk users). Not embeddable,
    # see comment on the top of the file
    'user_id': {
        'type':'objectid',
    },
    # `on_behalf_id` is not embeddable, see comment on the top of the file
    'on_behalf_id': {
        'type':'objectid',
        'data_relation': {
            'resource': 'users',
            'field': '_id',
        }
    },
    'coverages': {'type': 'dict'},
}
entity = {
    'schema': schema,
    'resource_methods': ['GET', 'POST'],
    'item_methods': ['GET', 'PUT', 'PATCH']
}
