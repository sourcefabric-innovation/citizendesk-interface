from unittest.mock import Mock, ANY

import citizendesk_interface.blueprints.proxy as proxy

core = 'http://localhost:9060'

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

@given('a request to fetch a twitter alias')
def fun(context):
    context.base.post('/proxy/fetch-citizen-alias/', {
        'name': 'Lukas',
        'authority': 'twitter'
    })

@then('the fetch request is forwarded to the core')
def fun(context):
    proxy.requests.post.assert_called_with(
        core + '/feeds/twt/citizen/alias/name/Lukas/request/',
        data='{}',
        headers=ANY
    )
