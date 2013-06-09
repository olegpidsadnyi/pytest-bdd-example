from flask import render_template


@app.route('/')
def index(template='dashboard.html'):
    return render_template(template)
