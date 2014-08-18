from .entities.reports import entity as reports
from .entities.twt_searches import entity as twt_searches
from .entities.twt_streams import entity as twt_streams
from .entities.twt_oauths import entity as twt_oauths
from .entities.twt_filters import entity as twt_filters
from .entities.steps import entity as steps
from .entities.settings_bool import entity as settings_bool
from .entities.settings_int import entity as settings_int
from .entities.settings_string import entity as settings_string
from .entities.coverages import entity as coverages
from .entities.core_config import entity as core_config
from .entities.citizen_lists import entity as citizen_lists
from .entities.citizen_aliases import entity as citizen_aliases

settings = {
    'SERVER_NAME': 'http://cd2.sourcefabric.net/citizendesk-interface',
    'MONGO_DBNAME': 'citizendesk',
    'X_DOMAINS': "*",
    'X_HEADERS': "Content-Type,If-Match,Authorization",
    'XML': False,
    'BANDWIDTH_SAVER': False,
    'CACHE_CONTROL': 'max-age=0, no-cache',
    'CACHE_EXPIRES': 0,
    'DATE_FORMAT': '%Y-%m-%dT%H:%M:%S+0000',
    # Superdesk wants this format
    'PAGINATION_DEFAULT': 100,
    'PAGINATION_LIMIT': 200,
             
    # even if dash separated is more common in URLs, i am using
    # underscore to separate words here. it is in the Python style and
    # it will work nicely with `eve-api` on the clien side. in
    # Javascript a dash separated object property has to be accessed
    # like in `obj['dash-separated']`, while an underscore separated
    # one will be accessible simply with `obj.underscore_separated`
    
    'DOMAIN': {
        'reports': reports,
        'twt_filters': twt_filters,
        'twt_oauths': twt_oauths,
        'twt-searches': twt_searches,
        'twt_streams': twt_streams,
        'steps': steps,
        'settings-bool': settings_bool,
        'settings-int': settings_int,
        'settings-string': settings_string,
        'coverages': coverages,
        'core_config': core_config,
        'citizen_lists': citizen_lists,
        'citizen_aliases': citizen_aliases,
    }
}
