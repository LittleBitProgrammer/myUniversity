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

from flask import render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
app.config['DEBUG'] = True
socketio = SocketIO(app)

users = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/orginate')
def orginate():
    socketio.emit('server orginated', 'Something happened on the server!')
    return '<h1>Sent!</h1>'

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


if __name__ == '__main__':
    socketio.run(app)