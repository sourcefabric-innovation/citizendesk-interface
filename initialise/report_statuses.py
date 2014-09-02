'''
Caveat: albeit being initialisation code, the values of the `key`
properties here are connected with the core, interface and frontend
code, and wrong values may lead to runtime errors. Modify with extreme
care and be sure to update the corresponding values in the code. Yeah
this is awful but i do not seem to have any choice at the
moment. Maybe one day the core will have internationalisation, so that
this collection and other workarounds will become superfluous
'''

from main import Init, init_collection

init_report_statuses = Init('report_statuses', [{
    'key': 'new',
    'direct': False,
    'description': 'This report is not verified yet'
}, {
    'key': 'assigned',
    'direct': False,
    'description': 'This report has been assigned for verification'
}, {
    'key': 'dismissed',
    'direct': True,
    'description': 'This report will not undergo verification'
}, {
    'key': 'debunked',
    'direct': True,
    'description': 'This report has been proven to be false!'
}, {
    'key': 'verified',
    'direct': True,
    'description': 'This report has been verified'
}, {
    # this status is not useful for its description. this is the value
    # that is set by the client side when the status is indirect. when
    # a status is indirect its value is not determined by the value of
    # the status property, but by other properties
    'key': '',
    'direct': True,
    'description': ''
}])

if __name__ == "__main__": init_collection(init_report_statuses)
