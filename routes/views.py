# Only common user views

# Web development imports
from flask import render_template

# Project imports
from index import app

@app.get('/')
def index():
    return render_template(
        'index.html'
    )