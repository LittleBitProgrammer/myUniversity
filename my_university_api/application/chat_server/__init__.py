from flask import Blueprint
from flask_socketio import emit
from flask import request
from application import socketio
from flask_cors import CORS
chat_blueprint = Blueprint('chat_blueprint', __name__, template_folder='templates', static_folder='static', static_url_path='static')
cors = CORS(chat_blueprint)
users = {}

@socketio.on('username', namespace='/private')
def receive_username(username):
    users[username] = request.sid
    print('Username added!')

@socketio.on('private_message', namespace='/private')
def private_message(payload):
    recipient_session_id = users[payload['username']]
    message = payload['message']
    emit('new_private_message', message, room=recipient_session_id)

from application.chat_server import routes

