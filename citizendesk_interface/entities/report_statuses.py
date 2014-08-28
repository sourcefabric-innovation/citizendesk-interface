'''
This collection has the purpose of keeping the translations for
citizendesk core, corresponding to every status for a report. The
descriptions will be added to the output generated for Live Blog
'''

entity = {
    'schema': {
        'key': {
            'type': 'string',
            'required': True,
            'unique': True,
            'allowed': [
                'new',
                'assigned',
                'debunked',
                'verified',
                'dismissed',
                ''
            ]
        },
        'description': {
            'type': 'string',
            'required': True
        },
        # Martin wants that some statuses are inferred from other
        # properties, in order to not duplicate information. I add
        # this `direct` property in order to make it clear to humans
        # which statuses can be directly assigned, and wich ones can
        # not. When a report transitions to an indirect status, its
        # `status` field has to be reset and the other relevant
        # properies have to be updated
        'direct': {
            'type': 'boolean',
            'required': True
        }
    },
    'resource_methods': ['GET'],
    'item_methods': ['GET', 'PATCH'],
    'pagination': False,
}
