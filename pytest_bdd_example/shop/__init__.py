from flask import Flask

from .settings import TEMPLATES_ROOT, MEDIA_ROOT


app = Flask(
    __name__,
    template_folder=TEMPLATES_ROOT,
    static_folder=MEDIA_ROOT,
)
