# This file contain all routes of mongodb

####################################################################
#                             import
####################################################################

from flask_restx import Resource, reqparse, fields  # to use Resource, that expose http request method
from api.mongodb.mongo_functions import *
from api.mongodb.models import *


@mongodb.route("/send_message")
class insertMessage(Resource):
    @mongodb.expect(send_message_model)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id_conversation', type=str, help='id_conversation')
        parser.add_argument('matricola_mittente', type=str, help='matricola_mittente')
        parser.add_argument('matricola_destinatario', type=str, help='matricola_destinatario')
        parser.add_argument('messaggio', type=str, help='messaggio')
        args = parser.parse_args(strict=True)
        send_message(args['id_conversation'], args['matricola_mittente'], args['matricola_destinatario'], args['messaggio'])

@mongodb.route("/create_new_conversation")
class createConversation(Resource):
    @mongodb.expect(conversation_model)
    @mongodb.marshal_with(id_conversation_model)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('matricola1', type=str, help='matricola1')
        parser.add_argument('matricola2', type=str, help='matricola2')
        args = parser.parse_args(strict=True)
        return create_conversation(args['matricola1'], args['matricola2']), 201


# ============================  get_all_conversations   ========================== #
@mongodb.route('/get_all_conversations')
class GetAllConversations(Resource):
    @mongodb.expect(freshman_model)
    @mongodb.marshal_with(full_conversation_model)
    def post(self):
        # arguments
        parser = reqparse.RequestParser()
        parser.add_argument('matricola', type=str, help='mat')
        args = parser.parse_args(strict=True)
        return get_all_conversations(args['matricola'],), 201