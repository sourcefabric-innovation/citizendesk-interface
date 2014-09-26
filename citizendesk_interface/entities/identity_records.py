entity = {
    'schema': {
        'first_name': {
            'type': 'string',
            'required': True
        },
        'last_name': {
            'type': 'string',
            'required': True
        },
        'email': {
            'type': 'string',
            'required': False
        },
        'location': {
            'type': 'string',
            'required': False
        },
        # handling the concurrency on the client side is tricky,
        # aliases may be associated to an identity while it has been
        # deleted elsewhere. for this reason i use the `deleted` flag,
        # so when an alias is associated with a deleted identity it is
        # still possible to detect the inconsistency and react
        'deleted': {
            'type': 'boolean'
        }
    },
    'resource_methods': ['GET', 'POST'],
    'item_methods': ['GET', 'PUT', 'PATCH'],
    'pagination': False
}
