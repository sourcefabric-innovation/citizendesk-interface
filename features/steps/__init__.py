'''
Implementations of steps wich are common among the different feature files
'''


@then('the request is successful')
def fun(context):
    """Assert a successful response"""
    code = context.response[1]
    assert code in (200, 201), 'Expected 20*, got {}'.format(code)
