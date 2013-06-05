#!/usr/bin/env python
from opster import command, dispatch

from .admin import admin
from .shop import shop


@command()
def runadmin(host=('a', '127.0.0.1', 'bind address')):
    admin.run(debug=True, host=host)


@command()
def runshop(host=('a', '127.0.0.1', 'bind address')):
    shop.run(debug=True, host=host)


if __name__ == '__main__':
    dispatch()
