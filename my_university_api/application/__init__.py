# This file is the entry point of our API, with the single import
# we launch the __init__.py of our module api
from flask import Flask
from config import Config
from flask_socketio import SocketIO

socketio = SocketIO(engineio_logger=True, logger=True, cors_allowed_origins='*')

def createApp(config_class=Config):
    app = Flask(__name__, static_folder=None)
    app.config.from_object(Config)
    socketio.init_app(app)

    from application.api import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')
    from application.chat_server import chat_blueprint
    app.register_blueprint(chat_blueprint, url_prefix='/chat')
    return app


if __name__ == '__main__':
    socketio.run(createApp, host='0.0.0.0')