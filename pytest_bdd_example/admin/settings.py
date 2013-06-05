import os

DEBUG = True
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

MEDIA_ROOT = os.path.join(BASE_PATH, 'media')
TEMPLATES_ROOT = os.path.join(BASE_PATH, 'templates', 'admin')

SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/pytestbdd-example.db'
