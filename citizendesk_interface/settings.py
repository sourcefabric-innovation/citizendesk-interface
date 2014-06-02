from .entities.reports import entity as reports
from .entities.twt_searches import entity as twt_searches
from .entities.steps import entity as steps

settings = {
    'MONGO_DBNAME': 'citizendesk',
    'X_DOMAINS': "*",
    'X_HEADERS': "Content-Type",
    'XML': False,
    'BANDWIDTH_SAVER': False,

    'DOMAIN': {
        'reports': reports,
        'twt_streams': {},
        'twt_filters': {},
        'twt_oauths': {},
        'twt-searches': twt_searches,
        'steps': steps,
        'settings-bool': {},
        'settings-int': {},
        'settings-string': {}
    }
}
