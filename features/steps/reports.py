from flask import json
from eve.tests import test_settings

def assert_success(code):
    """Assert a successful response"""
    assert code in (200, 201), 'Expected 20*, got {}'.format(code)

@given('one report assigned to user 1')
def fun(context):
    name = test_settings.MONGO_DBNAME
    doc = {
        'assignments': [{
                'user_id': '1'
        }]
    }
    context.base.connection[name]['reports'].remove()
    context.base.connection[name]['reports'].insert(doc)

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
