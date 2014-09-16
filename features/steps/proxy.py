from unittest.mock import Mock, ANY
import json

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

@given('a request to publish a report')
def fun(context):
    context.base.post('/proxy/publish/', {
        'report': 'report_id',
        'coverage': 'coverage_id'
    })

@then('the publish request is forwarded to the core')
def fun(context):
    proxy.requests.post.assert_called_with(
        core + '/feeds/any/report/id/report_id/publish/coverage_id/',
        data='{}',
        headers=ANY
    )

@given('a request to unpublish a report')
def fun(context):
    context.base.post('/proxy/unpublish/', {
        'report': 'report_id',
        'coverage': 'coverage_id'
    })

@then('the unpublish request is forwarded to the core')
def fun(context):
    proxy.requests.post.assert_called_with(
        core + '/feeds/any/report/id/report_id/unpublish/coverage_id/',
        data='{}',
        headers=ANY
    )

@given('a request to ingest from a location')
def fun(context):
    context.base.post('/proxy/ingest_from_location/', {
        'location': 'http://whatever.com',
        'user_id': 'abcdef'
    })

@then('the ingestion request is forwarded to the core')
def fun(context):
    proxy.requests.post.assert_called_with(
        core + '/ingest/url/feed/',
        data=ANY,
        headers=ANY
    )
    keyword_args = proxy.requests.post.call_args[1]
    data = json.loads(keyword_args['data'])
    context.base.assertIsNotNone(data)
    expected = {
        'url_link': 'http://whatever.com',
        'feed_name': 'frontend',
        'request_id': 'abcdef'
    }
    context.base.assertEqual(data, expected)
