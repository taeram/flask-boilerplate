from app import app
from flask import render_template
from flask.ext.login import login_required

@app.route('/', methods=['GET'])
@login_required
def index_home():
    return render_template('index/index.html')
