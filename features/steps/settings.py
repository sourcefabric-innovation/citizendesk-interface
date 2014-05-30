from flask import json
from eve.tests import test_settings

def assert_success(code):
    """Assert a successful response"""
    assert code in (200, 201), 'Expected 20*, got {}'.format(code)

@given('an enabled boolean setting in the database')
def fun(context):
    name = test_settings.MONGO_DBNAME
    doc = {
        'key': 'autoreply',
        'value': True
    }
    context.base.connection[name]['settings-bool'].insert(doc)
    context.last_id = doc['_id'];

@given('no boolean settings in the database')
def fun(context):
    name = test_settings.MONGO_DBNAME
    context.base.connection[name]['settings-bool'].remove()

@when('we create a new boolean setting')
def fun(context):
    data = {
        'key': 'autoreply',
        'value': True
    }
    url = '/settings-bool/'
    context.response = context.base.post(url, data)

@when('we update the boolean setting')
def fun(context):
    id = str(context.response[0]['_id'])
    etag = context.response[0]['_etag']
    data = {
        '_id': id,
        'key': 'autoreply',
        'value': True
    }
    url = '/settings-bool/{}'.format(id)
    headers = [( 'If-Match', etag )]
    context.response = context.base.put(url, data, headers=headers)

@then('the request is successful')
def fun(context):
    assert_success(context.response[1])

@then('we get the id in the request')
def fun(context):
    assert('_id' in context.response[0])
