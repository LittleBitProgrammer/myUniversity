# This file is the entry point of our API, with the single import
# we launch the __init__.py of our module api
from flask import Flask
from api import api_blueprint
from config import Config

# Creation of a Flask object
app = Flask(__name__)
# add config to our app
app.config.from_object(Config)
app.register_blueprint(api_blueprint, url_prefix='/api')