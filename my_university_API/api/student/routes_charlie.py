# This file contain all routes of student (This file is for Charlie)

####################################################################
#                             import
####################################################################
from flask_restx import Resource, reqparse, fields  # to use Resource, that expose http request method
from api.database_config import DatabaseConnector
from api.student.models_charlie import *
from api.student.db_funcz import *


database = DatabaseConnector('localhost', 'my_university_db', 'root', '')
connection = database.get_connection()

# ============================    richiesta ricevimento   ========================== #
@student.route('/richiesta_ricevimento')
class InsertRichiestaRicevimento(Resource):
    @student.expect(insert_richiesta_ricevimento_model)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('matricola_docente', type=str, help='matricola_docente')
        parser.add_argument('data_ricevimento', type=str, help='data_ricevimento')
        parser.add_argument('matricola_studente', type=str, help='matricola_studente')
        parser.add_argument('motivazione_ricevimento', type=str, help='motivazione_ricevimento')
        args = parser.parse_args(strict=True)
        insert_richiesta_ricevimento(args['matricola_docente'],
                                     args['data_ricevimento'],
                                     args['matricola_studente'],
                                     args['motivazione_ricevimento'],
                                     connection)


# ============================    cancella ricevimento   ========================== #
@student.route('/cancella_richiesta_ricevimento')
class DelRequestReceipt(Resource):
    @student.expect(delete_richiesta_ricevimento_model)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('matricola_docente', type=str, help='matricola_docente')
        parser.add_argument('data_ricevimento', type=str, help='data_ricevimento')
        parser.add_argument('matricola_studente', type=str, help='matricola_studente')
        args = parser.parse_args(strict=True)
        delete_richiesta_ricevimento(args['matricola_docente'],
                                     args['data_ricevimento'],
                                     args['matricola_studente'],
                                     connection)

# ============================    iscrizione_newletter   ========================== #
@student.route('/iscrizione_newsletter')
class IscrizioneNewsletter(Resource):
    @student.expect(insert_iscrizione_newsletter_model)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('codice_corso', type=str, help='codice_corso')
        parser.add_argument('codice_disciplina', type=str, help='codice_disciplina')
        parser.add_argument('matricola_studente', type=str, help='matricola_studente')
        parser.add_argument('data_iscrizione', type=str, help='data_iscrizione')
        args = parser.parse_args(strict=True)
        insert_iscrizione_newsletter(args['codice_corso'],
                                     args['codice_disciplina'],
                                     args['matricola_studente'],
                                     args['data_iscrizione'],
                                     connection)

# ============================    avvisi   ========================== #
@student.route('/avvisi')
class SubmitNewsletter(Resource):
    @student.expect(freshman_student)
    @student.marshal_with(get_news_student_model)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('matricola_studente', type=str, help='matricola_studente')
        args = parser.parse_args(strict=True)
        return reperimento_news_studente(args['matricola_studente'], connection), 201


# ============================    lista prenotazioni ricevimento   ========================== #
@student.route('/lista_prenotazioni_ricevimento')
class ListaPrenotazioniRIcevimento(Resource):
    @student.expect(freshman_student)
    @student.marshal_with(get_prenotazioni_ricevimento_model)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('matricola_studente', type=str, help='matricola_studente')
        args = parser.parse_args(strict=True)
        return reperimento_prenotazioni_ricevimento_studente(args['matricola_studente'], connection), 201

