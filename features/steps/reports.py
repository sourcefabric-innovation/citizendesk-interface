from flask import json

def assert_success(code):
    """Assert a successful response"""
    assert code in (200, 201), 'Expected 20*, got {}'.format(code)

@when('we ask reports')
def impl(context):
    context.response = context.base.get('reports')

@then('we get reports')
def impl(context):
    assert_success(context.response[1])
    l = len(context.response[0])
    assert l == 2, 'length is {}'.format(l)
