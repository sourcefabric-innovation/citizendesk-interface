schema = {
    'channel': {
        'type': 'list',
        'allowed': ["citizendesk-frontend", "twitter", "sms"],
    },
    'content': {
        'type': 'string',
    },
}
entity = {
    'schema': schema,
    'resource_methods': ['GET', 'POST'],
}
