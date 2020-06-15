from application.chat_server import socketio, chat_blueprint
from flask import render_template
from flask_cors import CORS, cross_origin

cors = CORS(chat_blueprint)

@chat_blueprint.route('/')
@cross_origin()
def index():
    return render_template('index.html')

@chat_blueprint.route('/orginate')
def orginate():
    socketio.emit('server orginated', 'Something happened on the server!')
    return '<h1>Sent!</h1>'

