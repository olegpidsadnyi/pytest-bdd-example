#!/usr/bin/env python

from flask.ext.script import Manager, Shell, Server, Command

from pytest_bdd_example.dashboard import app as dashboard_app
from pytest_bdd_example.shop import app as shop_app


def create_app(app=None):
    APPS = {
        'dashboard': dashboard_app,
        'shop': shop_app,
    }

    return APPS[app]

manager = Manager(create_app)
manager.add_option("-app", "--application", dest="app", required=True)
manager.add_command("runserver", Server("127.0.0.1"))
manager.add_command("shell", Shell(use_ipython=True))
manager.run()