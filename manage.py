#!/usr/bin/env python
from flask.ext.script import Manager, Shell, Server

from pytest_bdd_example import dashboard
from pytest_bdd_example import shop


def create_app(app=None):
    APPS = {
        'dashboard': dashboard.app,
        'shop': shop.app,
    }

    return APPS[app]

manager = Manager(create_app)


manager.add_option('-app', '--application', dest='app', required=True)
manager.add_command('runserver', Server('127.0.0.1'))
manager.add_command('shell', Shell(use_ipython=True))


@manager.command
def mkdb():
    from tests.helpers.mkdb.db import recreate_database
    from tests.helpers.mkdb.initialdata import create_initial_data
    recreate_database()
    create_initial_data()

if __name__ == '__main__':
    manager.run()

