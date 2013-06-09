from flask import Flask

# from flask.ext.admin import Admin


from pytest_bdd_example.dashboard import settings

from pytest_bdd_example import auth


app = Flask(
    __name__,
    static_folder=settings.MEDIA_ROOT,
    template_folder=settings.TEMPLATES_ROOT,
)
app.config.from_object('pytest_bdd_example.dashboard.settings')
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


app.register_blueprint(auth.bp, url_prefix='/auth')
