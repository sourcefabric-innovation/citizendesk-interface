from eve.tests import test_settings
from bson import objectid

alias_id = '53f711499c6167315a536b45'
list_id = '53f6fff79c61670c2b57f93d'
list_name = 'friends of friends'
list = {
    '_id': objectid.ObjectId(list_id),
    'variation': "label-primary",
    'name': list_name
}
alias = {
    '_id': objectid.ObjectId(alias_id),
    'tags': [
        list_id
    ],
    'identifiers': {},
    'authority': "twitter",
}
database = test_settings.MONGO_DBNAME

@given('a list')
def fun(context):
    context.base.connection[database]['citizen_lists'].remove()
    context.base.connection[database]['citizen_lists'].insert(list)

@given('an alias referring to it')
def fun(context):
    context.base.connection[database]['citizen_aliases'].remove()
    context.base.connection[database]['citizen_aliases'].insert(alias)

@when('we ask for the alias with the embedded list')
def fun(context):
    context.alias, _ = context.base.get(
        'citizen_aliases',
        item=alias_id,
        query='?embedded={"tags":1}'
    )

@when('we ask for aliases')
def fun(context):
    context.response, _ = context.base.get('citizen_aliases')

@given('one alias')
def fun(context):
    context.base.connection[database]['citizen_aliases'].remove()
    context.base.connection[database]['citizen_aliases'].insert(alias)

@when('we ask for that alias')
def fun(context):
    context.alias, _ = context.base.get('citizen_aliases', item=alias_id)

@when('we ask for that alias with embedded lists')
def fun(context):
    context.alias, _ = context.base.get(
        'citizen_aliases',
        item=alias_id,
        query='?embedded={"tags":1}'
    )

@then('we get the alias')
def fun(context):
    error = 'response is {}'.format(context.alias)
    assert '_id' in context.alias, error
    assert context.alias['_id'] == alias_id, error

@then('we get the alias in the collection')
def fun(context):
    error = 'response is {}'.format(context.response)
    assert context.response['_items'][0]['_id'] == alias_id, error

@then('we get tags in the alias')
def fun(context):
    error = 'response is {}'.format(context.alias)
    assert 'tags' in context.alias, error

@then('we get the alias with the embedded list')
def fun(context):
    tags = context.alias['tags']
    assert tags[0]['name'] == list_name, 'tags is {}'.format(tags)
