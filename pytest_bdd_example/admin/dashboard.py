from flask import render_template
from __package__ import app


@app.route('/')
def dashboard():
    return render_template('dashboard.html')
