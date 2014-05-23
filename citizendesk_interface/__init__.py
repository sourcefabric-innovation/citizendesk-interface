from eve import Eve

from .settings import settings as default_settings

app = Eve(settings=default_settings)

def get_app(customised):
    settings = default_settings.copy()
    settings.update(customised)
    return Eve(settings=settings)
