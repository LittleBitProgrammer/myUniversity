from flask import Blueprint
from flask_socketio import emit
from flask import request
from application import socketio

chat_blueprint = Blueprint('chat_blueprint', __name__, template_folder='templates', static_folder='static')

users = {}

@socketio.on('message from user', namespace='/messages')
def receive_message_from_user(message):
    print('USER MESSAGE: {}'.format(message))
    emit('from flask', message.upper(), broadcast=True)

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

