from flask_restx import fields
from application.api.mongodb import *

freshman_model = mongodb.model('freshman', {
    'matricola': fields.String
})

id_conversation_model = mongodb.model('id_conversation_model', {
    'id_conversation': fields.String
})

send_message_model = mongodb.model('insert_message', {
    'id_conversation': fields.String,
    'matricola_mittente': fields.String,
    'matricola_destinatario': fields.String,
    'messaggio': fields.String
})

get_message_model = mongodb.model('get_messages', {
    'matricola_mittente': fields.String,
    'matricola_destinatario': fields.String,
    'messaggio': fields.String,
    'data_invio': fields.String
})

conversation_model = mongodb.model('conversation_model', {
    'matricola1': fields.String,
    'matricola2': fields.String
})

full_conversation_model = mongodb.model('full_conversation_model', {
    'id_conversation': fields.String,
    'matricola1': fields.String,
    'matricola2': fields.String,
    'messages': fields.List(fields.Nested(get_message_model))
})

discipline_color_model = mongodb.model('discipline_color_model', {
    'codice_corso': fields.String,
    'codice_disciplina': fields.String,
    'colore_esadecimale': fields.String
})