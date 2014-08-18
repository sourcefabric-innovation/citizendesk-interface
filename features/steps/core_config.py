from eve.tests import test_settings

@given('no docs in the core config collection')
def fun(context):
    name = test_settings.MONGO_DBNAME
    context.base.connection[name]['core_config'].remove()

@when('we create a new invented doc')
def fun(context):
    data = {
        'type': 'invented',
        'set': {}
    }
    url = '/core_config/'
    context.response = context.base.post(url, data)

@given('an sms doc in the database')
def fun(context):
    name = test_settings.MONGO_DBNAME
    doc = {
        'type': 'sms',
        'set': {
            'whatever': True
        }
    }
    context.base.connection[name]['core_config'].remove()
    context.base.connection[name]['core_config'].insert(doc)

@when('we fetch the sms doc')
def fun(context):
    query = 'core_config?where={"type":"sms"}'
    context.response = context.base.get(query)

@when('we update the sms doc')
def fun(context):
    doc = context.response[0]['_items'][0]
    id = doc['_id']
    etag = doc['_etag']
    data = {
        'type': 'sms',
        'set': {}
    }
    url = '/core_config/{}'.format(id)
    headers = [( 'If-Match', etag )]
    context.response = context.base.put(url, data, headers=headers)
