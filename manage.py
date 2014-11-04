from flask.ext.script import Manager
from apps.auth.db.commands import CreateUserCommand
from apps.auth.db.commands import HashUserPasswordsCommand

from citizendesk_interface import app

manager = Manager(app)

if __name__ == "__main__":
    manager.run({
        'create-user': CreateUserCommand(),
        'hash-user-passwords': HashUserPasswordsCommand()
    });
