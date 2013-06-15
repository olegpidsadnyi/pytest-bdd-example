from flask import redirect, url_for

from .app import app


@app.route('/')
def index():
    return redirect(url_for('admin.index'))
