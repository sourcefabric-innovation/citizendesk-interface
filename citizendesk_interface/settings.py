from .entities.reports import entity as reports
from .entities.twt_searches import entity as twt_searches
from .entities.steps import entity as steps
from .entities.settings_bool import entity as settings_bool
from .entities.settings_int import entity as settings_int
from .entities.settings_string import entity as settings_string

settings = {
    'MONGO_DBNAME': 'citizendesk',
    'X_DOMAINS': "*",
    'X_HEADERS': "Content-Type,If-Match",
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
        'settings-string': {},
        'steps': {},
        'settings-bool': settings_bool,
        'settings-int': settings_int,
        'settings-string': settings_string,
    }
}
