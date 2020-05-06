# This file contain all routes of professor

####################################################################
#                             import
####################################################################

from flask_restx import Resource, reqparse, fields  # to use Resource, that expose http request method
from api import professor
from api.professor.database_functions import loginProfessor
from api.professor.models import *
from api.database_config import DatabaseConnector
from mysql.connector import Error
import mysql.connector

database = DatabaseConnector('localhost', 'my_university_db', 'root', '')
connection = database.get_connection()

####################################################################
#                             routing
####################################################################
# ============================    login    ========================== #
@professor.route('/login')
class Login(Resource):
    @professor.expect(login_professor)
    @professor.marshal_with(professor_model)
    def post(self):
        # arguments
        parser = reqparse.RequestParser()
        parser.add_argument('matricola_docente', type=str, help='mat of professor')
        parser.add_argument('password_docente', type=str, help='mat of professor')
        args = parser.parse_args(strict=True)

        return loginProfessor(args['matricola_docente'], args['password_docente'], connection), 201





# ============================    password    ========================== #
@professor.route('/password')
class Password(Resource):
    def post(self):
        return {'password': '1'}


# ============================    get contatti    ========================== #
@professor.route('/contatti')
class GetContact(Resource):
    def post(self):
        return {'contatti': '1'}


# ============================    delete contatto    ========================== #
@professor.route('/contatto_docente')
class DelContact(Resource):
    def post(self):
        return {'contatto': '1'}


# ============================    assunzione    ========================== #
@professor.route('/assunzioni')
class Assumption(Resource):
    def post(self):
        return {'assunzioni': '1'}


# ============================    insegnamento    ========================== #
@professor.route('/insegnamenti')
class Teaching(Resource):
    def post(self):
        return {'insegnamenti': '1'}


# ============================    post lezione    ========================== #
@professor.route('/lezione')
class Lesson(Resource):
    def post(self):
        return {'lezione': '1'}


# ============================    cancella lezione    ========================== #
@professor.route('/cancella_lezione')
class DelLesson(Resource):
    def post(self):
        return {'lezione': '1'}


# ============================   get lezioni    ========================== #
@professor.route('/lezioni')
class GetLesson(Resource):
    def post(self):
        return {'lezioni': '1'}


# ============================  avviso   ========================== #
@professor.route('/avviso')
class Alert(Resource):
    def post(self):
        return {'avviso': '1'}


# ============================  cancella avviso   ========================== #
@professor.route('/cancella_avviso')
class DelAlert(Resource):
    def post(self):
        return {'avviso': '1'}


# ============================  avvisi   ========================== #
@professor.route('/avvisi')
class Alerts(Resource):
    def post(self):
        return {'avvisi': '1'}


# ============================  ricevimento   ========================== #
@professor.route('/ricevimento')
class Receipt(Resource):
    def post(self):
        return {'ricevimento': '1'}


# ============================  update ricevimento   ========================== #
@professor.route('/aggiorna_ricevimento')
class UPReceipt(Resource):
    def post(self):
        return {'ricevimento': '1'}


# ============================  cancella ricevimento   ========================== #
@professor.route('/cancella_ricevimento')
class DelReceipt(Resource):
    def post(self):
        return {'ricevimento': '1'}


# ============================ richiesta ricevimento   ========================== #
@professor.route('/ricevimenti')
class Receipts(Resource):
    def post(self):
        return {'ricevimenti': '1'}


# ============================    calendario   ========================== #
@professor.route('/calendario')
class Calendario(Resource):

    def post(self):
        return {'iscrizione newsletter': '1'}