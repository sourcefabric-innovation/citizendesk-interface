from uuid import uuid1

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
                    'type': 'objectid',
                    'data_relation': {
                        'resource': 'users',
                        'field': '_id',
                        'embeddable': True
                    }
                }
            }
        }
    },
    'original': {'type': 'dict'},
    'produced': {
        'type': 'datetime',
        'required': True
    },
    'texts': {'type': 'list'},
    'verified': {'type':'boolean'},
    'summary': {'type':'boolean'},
    'proto': {'type':'boolean'},
    'automatic': {'type':'boolean'},
    'feed_type': {
        'type':'string',
        'allowed': ['tweet', 'sms', 'plain', 'web_link']
    },
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
    },
    'on_behalf_id': {
        'type':'objectid',
        'data_relation': {
            'resource': 'users',
            'field': '_id',
            'embeddable': True
        }
    },
    'status': {
        'type':'string',
        # just direct statuses and the null status are allowed
        'allowed': [
            'dismissed',
            'debunked',
            'verified',
            ''
        ],
        'data_relation': {
            'resource': 'report_statuses',
            'field': 'key',
        }
    },
    'status_updated': {
        'type': 'datetime'
    },
    'coverages': {
        'type': 'dict',
        'schema': {
            'outgested': {
                'type': 'list',
                'schema': {
                    'type': 'string',
                }
            },
            'targeting': {
                'type': 'list',
                'schema': {
                    'type': 'string',
                }
            },
            'published': {
                'type': 'list',
                'schema': {
                    'type': 'string',
                }
            }
        }
    },
    'media': {
        'type': 'list',
        'schema': {
            'link': {
                'type': 'string'
            }
        }
    },
    'notices_outer': {
        'type': 'list',
        'schema': {
            'type': 'string'
        }
    }
}
entity = {
    'schema': schema,
    'resource_methods': ['GET', 'POST'],
    # DELETE introduced in order to delete session summaries
    'item_methods': ['GET', 'PUT', 'PATCH', 'DELETE']
}

def on_insert_reports(items):
    for item in items:
        item['report_id'] = str(uuid1())

def init(app):
    app.on_insert_reports += on_insert_reports
