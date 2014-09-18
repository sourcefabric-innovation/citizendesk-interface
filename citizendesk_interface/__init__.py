import logging

from eve import Eve
from eve.io.mongo import MongoJSONEncoder
from eve.render import send_response
from raven.handlers.logging import SentryHandler
import superdesk

try:
    from eve_docs import eve_docs
    from flask.ext.bootstrap import Bootstrap
    has_docs = True
except ImportError:
    has_docs = False

from .entities.twt_oauths import init as citizendesk_oauths_init_app
from .entities.reports import init as citizendesk_reports_init_app
from .entities.coverages import init as citizendesk_coverages_init_app
from .settings import settings as default_settings
from .blueprints.proxy import blueprint as proxy_blueprint

handler = SentryHandler('http://b1901abf077d476ba253bce45dd5bf91:cf99fe3dade94a599e9a79aada3f6266@sentry.sourcefabric.org/8')
#logger = logging.getLogger('citizendesk')
#logger.addHandler(handler)

def register_blueprints(app):
    app.register_blueprint(proxy_blueprint, url_prefix='/proxy')
    citizendesk_oauths_init_app(app)
    citizendesk_reports_init_app(app)
    citizendesk_coverages_init_app(app)
    if has_docs:
        Bootstrap(app) # required by eve docs
        app.register_blueprint(eve_docs, url_prefix='/docs')

def get_app(customised={}):
    settings = default_settings.copy()
    settings.update(customised)
    app = Eve(
        settings=settings,
        json_encoder=MongoJSONEncoder
    )
    register_blueprints(app)
    app.logger.addHandler(handler)
    @app.errorhandler(superdesk.SuperdeskError)
    def error_handler(error):
        """Return json error response.

        :param error: an instance of :attr:`superdesk.SuperdeskError` class
        """
        return send_response(
            None,
            (error.to_dict(), None, None, error.status_code)
        )
    return app

app = get_app()
