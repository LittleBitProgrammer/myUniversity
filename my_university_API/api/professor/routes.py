# This file contain all routes of professor

####################################################################
#                             import
####################################################################
from api.professor import professor  # to use api
from flask_restx import Resource  # to use Resource, that expose http request method


####################################################################
#                             routing
####################################################################
# ============================    login    ========================== #
@professor.route('/login')
class Login(Resource):
    def post(self):
        return {'login': '1'}


# ============================    password    ========================== #
@professor.route('/password')
class Password(Resource):
    def post(self):
        return {'password': '1'}


# ============================    inserimento contatto    ========================== #
@professor.route('/contatto')
class Contact(Resource):
    def post(self):
        return {'contatto': '1'}


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

    def delete(self):
        return {'lezione': '2'}


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

    def delete(self):
        return {'avviso': '2'}


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

    def delete(self):
        return {'ricevimento': '2'}

    def update(self):
        return {'ricevimento': '3'}


# ============================ richiesta ricevimento   ========================== #
@professor.route('/ricevimenti')
class Receipt(Resource):
    def post(self):
        return {'ricevimenti': '1'}