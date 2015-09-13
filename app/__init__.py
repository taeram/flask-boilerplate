# Application
from flask import Flask
app = Flask(__name__, template_folder="views/templates")
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

# Database
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

# Environment
from os import getenv
if getenv('FLASK_ENV') == 'production':
    app.config.from_object('config.ProductionConfig')
else:
    app.config.from_object('config.DevelopmentConfig')

# Import the controllers
from .controllers import *
from .controllers.helpers import *
from .views.helpers.filters import *
