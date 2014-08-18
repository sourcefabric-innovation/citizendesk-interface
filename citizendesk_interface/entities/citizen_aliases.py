entity = {
    'schema': {
        'authority': {
            'type': 'string'
        },
        'identifiers': {
            'type': 'dict',
            'schema': {
                'user_name_search': {
                    'type': 'string'
                },
                'user_name': {
                    'type': 'string'
                },
                'user_id': {
                    'type': 'string'
                },
                'user_id_search': {
                    'type': 'string'
                },
            },
        },
        'tags': {
            'type': 'list',
            'schema': {
                'type': 'objectid',
                'data_relation': {
                    'resource': 'citizen_lists',
                    'field': '_id',
                    'embeddable': True,
                },
            },
        },
        'avatars': {
            'type': 'list',
            'schema': {
                'https': {
                    'type': 'string'
                },
            },
        },
    },
    'resource_methods': ['GET'],
    'item_methods': ['GET', 'PATCH'],
    'pagination': False,
}
