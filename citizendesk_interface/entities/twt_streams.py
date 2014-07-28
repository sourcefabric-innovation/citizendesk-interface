entity = {
    'schema': {
        'user_id': {
            'type': 'objectid',
            'data_relation': {
                'resource': 'users',
                'field': '_id',
                'embeddable': True
            }
        },
        'spec': {
            'type': 'dict',
            'schema': {
                'filter_id': {
                    'type': 'objectid',
                    'data_relation': {
                        'resource': 'twt_filters',
                        'field': '_id',
                        'embeddable': True
                    }
                },
                'oauth_id': {
                    'type': 'objectid',
                    'data_relation': {
                        'resource': 'twt_oauths',
                        'field': '_id',
                        'embeddable': True
                    }
                }
            }
        }
    },
    'resource_methods': ['GET', 'POST'],
    'item_methods': ['GET', 'DELETE'],
    'pagination': False
}
