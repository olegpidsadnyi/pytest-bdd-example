#!/usr/bin/env python
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name='pytest-bdd-example',
    description='pytest-bdd example application',
    author='Oleg Pidsadnyi',
    author_email='oleg.podsadny@gmail.com',
    version='0.1',
    cmdclass={'test': PyTest},
    install_requires=[
        'flask-admin',
        'flask-script',
        'flask-login',
        'flask-security',
        'flask-sqlalchemy',
    ],
    tests_require=[
        'pytest-bdd-splinter',
    ],
    packages=['pytest_bdd_example'],
)
