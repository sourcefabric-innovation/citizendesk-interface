from flask.ext.script import Manager
from apps.auth.db.commands import CreateUserCommand

from citizendesk_interface import app

manager = Manager(app)

if __name__ == "__main__":
    manager.run({'create-user': CreateUserCommand()})
