from flask import Flask

from .settings import TEMPLATES_ROOT, MEDIA_ROOT
from ..auth import bp as bp_auth


app = Flask(
    __name__,
    template_folder=TEMPLATES_ROOT,
    static_folder=MEDIA_ROOT,
)

app.register_blueprint(bp_auth, url_prefix='/auth')
