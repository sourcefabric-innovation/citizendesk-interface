from flask import json
from eve.tests import test_settings
from bson.objectid import ObjectId

name = test_settings.MONGO_DBNAME

def assert_success(code):
    """Assert a successful response"""
    assert code in (200, 201), 'Expected 20*, got {}'.format(code)

@given('one report assigned to user 1')
def fun(context):
    doc = {
        'assignments': [{
                'user_id': '1'
        }]
    }
    context.base.connection[name]['reports'].remove()
    context.base.connection[name]['reports'].insert(doc)

@given('no reports')
def fun(context):
    context.base.connection[name]['reports'].remove()

@when('we ask reports')
def impl(context):
    context.response = context.base.get('reports')

@when('we ask reports assigned to user id 1')
def fun(context):
    query = 'reports?where={"assignments.user_id":"1"}'
    context.response = context.base.get(query)

@when('we ask reports assigned to user id 2')
def fun(context):
    query = 'reports?where={"assignments.user_id":"2"}'
    context.response = context.base.get(query)

@then('we get an empty list')
def impl(context):
    assert_success(context.response[1])
    l = len(context.response[0]['_items'])
    assert l == 0, 'length is {}'.format(l)

@then('we get the assigned report')
def fun(context):
    assert_success(context.response[1])
    l = len(context.response[0]['_items'])
    assert l == 1, 'length is {}'.format(l)


@when('we insert a report')
def fun(context):
    context.response = context.base.post('/reports/', {
        'texts': [],
        'summary': False,
        'session': 'abcd',
        'channels': [{
            'type': 'frontend'
        }],
        'produced': '2014-08-01T13:53:44.040Z',
        'user_id': '53db9be89c6167205b8f44fb',
        'authors': [{
            'authority': 'citizen_desk',
            'identifiers': ''
        }],
        'assignments': [],
        'feed_type': 'plain',
        'automatic': False,
        'local': True,
        'proto': False,
      })
    context.posted = context.response[0]

@when('we modify the inserted report')
def fun(context):
    context.response = context.base.patch(
        '/reports/{}'.format(context.posted['_id']),
        data={'notices_outer': ['just a comment']},
        headers=[('If-Match', context.posted['_etag'])]
    )
    context.patched = context.response[0]

@when('we get the inserted report')
def fun(context):
    context.response = context.base.get(
        'reports',
        item=context.posted['_id']
    )
    context.gotten = context.response[0]

@then('the report entity tag is updated upon change')
def fun(context):
    patched_etag = context.patched['_etag']
    gotten_etag  = context.gotten['_etag']
    assert patched_etag == gotten_etag, 'patch tag: {}, get tag: {}'.format(
        patched_etag,
        gotten_etag
    )

@then('the report gets a report id')
def fun(context):
    id = context.response[0]['_id']
    report = context.base.connection[name]['reports'].find_one(ObjectId(id))
    assert 'report_id' in report, report
