import os

from eve.tests import TestMinimal

from citizendesk_interface import register_blueprints

# https://github.com/nicolaiarocci/eve/blob/develop/eve/tests/__init__.py
class TestBase(TestMinimal):
    def setUp(self):
        this_directory = os.path.dirname(os.path.realpath(__file__))
        # Load the settings file, using a robust path
        settings_file = os.path.join(this_directory, 'test_settings.py')

        super(TestBase, self).setUp(settings_file)

def before_all(context):
    context.base = TestBase()
    context.base.setUp()
    register_blueprints(context.base.app)

def after_all(context):
    context.base.tearDown()

# -- FILE: features/environment.py
# USE: BEHAVE_DEBUG_ON_ERROR=yes     (to enable debug-on-error)
from distutils.util import strtobool as _bool

BEHAVE_DEBUG_ON_ERROR = _bool(os.environ.get("BEHAVE_DEBUG_ON_ERROR", "no"))

def after_step(context, step):
    if BEHAVE_DEBUG_ON_ERROR and step.status == "failed":
        # -- ENTER DEBUGGER: Zoom in on failure location.
        import pdb
        pdb.post_mortem(step.exc_traceback)
