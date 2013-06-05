import os

DEBUG = True
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

MEDIA_ROOT = os.path.join(BASE_PATH, 'media')
TEMPLATES_ROOT = os.path.join(BASE_PATH, 'templates', 'shop')

SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/pytestbdd-example.db'
