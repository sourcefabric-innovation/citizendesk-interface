'''
Implementations of steps wich are common among the different feature files
'''


@then('the request is successful')
def fun(context):
    """Assert a successful response"""
    code = context.response[1]
    assert code in (200, 201), 'Expected 20*, got {}, {}'.format(
        code,
        context.response
    )

@then('the request fails')
def fun(context):
    """Assert a successful response"""
    code = context.response[1]
    assert code not in (200, 201), 'Expected failure, got {}'.format(code)

@then('we get the id in the response')
def fun(context):
    assert('_id' in context.response[0])

@then('we get a list containing one document')
def fun(context):
    l = len(context.response[0]['_items'])
    assert l == 1, 'length is {}'.format(l)
