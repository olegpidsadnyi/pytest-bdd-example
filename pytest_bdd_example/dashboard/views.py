from flask import render_template

from .app import app


@app.route('/')
def index(template='dashboard.html'):
    return render_template(template)
