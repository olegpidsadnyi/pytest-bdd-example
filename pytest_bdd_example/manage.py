#!/usr/bin/env python

from flask.ext.script import Manager, Shell, Server

from pytest_bdd_example import app

manager = Manager(app)

manager.add_command("runserver", Server("127.0.0.1"))
manager.add_command("shell", Shell(use_ipython=True))
manager.run()