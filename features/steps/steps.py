
@when('we create a new step')
def fun(context):
    context.response = context.base.post('/steps/', {
            'description': 'any kind of description'
    })
