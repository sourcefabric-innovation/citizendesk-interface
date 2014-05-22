from flask import json

def assert_200(response):
    """Assert we get status code 200."""
    code = response.status_code
    assert code in (200, 201), 'Expected 20*, got {}'.format(code)

@when('we ask reports')
def impl(context):
    context.response = context.app.get('/reports')

@then('we get reports')
def impl(context):
    assert_200(context.response)
    l = len(json.loads(context.response.get_data()))
    assert l == 2, 'length is {}'.format(l)
