from flask import json
from eve.tests import test_settings

@given('a key in the database')
def fun(context):
    name = test_settings.MONGO_DBNAME
    doc = {
        "spec" : {
            "consumer_secret" : "GYJYiQNxhwDqEGSljhg",
            "access_token_key" : "1960324645-eJNCBnb",
            "consumer_key" : "X7twExDgXJ",
            "access_token_secret" : "gg2IqR8NTBCBTG6eCiFGmP",
        }
    }
    context.base.connection[name]['twt_oauths'].remove()
    context.base.connection[name]['twt_oauths'].insert(doc)

@when('the user asks for the key')
def fun(context):
    context.response = context.base.get('twt_oauths')

@then('he gets masked values')
def fun(context):
    l = len(context.response[0]['_items'])
    assert l == 1, 'length is {}'.format(l)
    sec = context.response[0]['_items'][0]['spec']['consumer_secret'];
    assert sec == '****************jhg', 'consumer secret is {}'.format(sec)
