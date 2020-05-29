# This file is the entry point of our API, with the single import
# we launch the __init__.py of our module api
from flask import Flask
from config import Config
from flask_socketio import SocketIO

socketio = SocketIO()

def createApp(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    socketio.init_app(app)

    from application.api import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')
    from application.chat_server import chat_blueprint
    app.register_blueprint(chat_blueprint, url_prefix='/chat')
    return app


