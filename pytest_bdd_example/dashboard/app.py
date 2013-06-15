from flask import Flask

from flask.ext.sqlalchemy import SQLAlchemy
from pytest_bdd_example.dashboard import settings


app = Flask(
    __name__,
    static_folder=settings.MEDIA_ROOT,
    template_folder=settings.TEMPLATES_ROOT,
)

app.config.from_object('pytest_bdd_example.dashboard.settings')
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


db = SQLAlchemy(app)

with app.app_context():
    from pytest_bdd_example.auth import auth
    from pytest_bdd_example.book import book

    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(book)
