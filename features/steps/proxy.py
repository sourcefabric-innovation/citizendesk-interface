from unittest.mock import Mock

import citizendesk_interface.blueprints.proxy as proxy

response = Mock(
    raise_for_status=lambda :None,
    text='{}',
    status_code=200
)
proxy.requests.post = Mock(return_value=response)

@given('a request to start a twitter search')
def fun(context):
    context.response = context.base.post('/proxy/start-twitter-search/', {
        'whatever':True
    })
    
@then('the request is forwarded to the core')
def fun(context):
    assert proxy.requests.post.called, 'the mocked post was not called'
