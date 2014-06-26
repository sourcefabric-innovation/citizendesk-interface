import logging

from eve import Eve
from eve.io.mongo import MongoJSONEncoder
from raven.handlers.logging import SentryHandler
import superdesk.users as superdesk_users
import superdesk.auth as superdesk_auth
from eve_docs import eve_docs
from flask.ext.bootstrap import Bootstrap

from .settings import settings as default_settings
from .blueprints.proxy import blueprint as proxy_blueprint

handler = SentryHandler('http://b1901abf077d476ba253bce45dd5bf91:cf99fe3dade94a599e9a79aada3f6266@sentry.sourcefabric.org/8')
#logger = logging.getLogger('citizendesk')
#logger.addHandler(handler)

def register_blueprints(app):
    app.register_blueprint(proxy_blueprint, url_prefix='/proxy')
    superdesk_users.init_app(app)
    superdesk_auth.init_app(app)
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
    return app

app = get_app()
