from uuid import uuid1

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
        'allowed': ['tweet', 'sms', 'plain', 'link']
    },
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
            # careful with embedding, may be null
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
                    'type': 'objectid',
                    'data_relation': {
                        'resource': 'coverages',
                        'field': '_id'
                    }
                }
            },
            'targeting': {
                'type': 'list',
                'schema': {
                    'type': 'objectid',
                    'data_relation': {
                        'resource': 'coverages',
                        'field': '_id'
                    }
                }
            },
            'published': {
                'type': 'list',
                'schema': {
                    'type': 'objectid',
                    'data_relation': {
                        'resource': 'coverages',
                        'field': '_id'
                    }
                }
            }
        }
    },
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
