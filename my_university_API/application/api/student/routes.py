# This file contain all routes of student (This file is for Charlie)

####################################################################
#                             import
####################################################################
from flask_restx import Resource, reqparse, fields  # to use Resource, that expose http request method
from application.api.database_config import DatabaseConnector
from application.api.student.models import *
from application.api.student.database_functions import *


database = DatabaseConnector('localhost', 'my_university_db', 'root', '')

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
                                     database.get_connection())


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
                                     database.get_connection())

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
                                     database.get_connection())

# ============================    avvisi   ========================== #
@student.route('/avvisi')
class SubmitNewsletter(Resource):
    @student.expect(freshman_student)
    @student.marshal_with(get_news_student_model)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('matricola_studente', type=str, help='matricola_studente')
        args = parser.parse_args(strict=True)
        return reperimento_news_studente(args['matricola_studente'], database.get_connection()), 201


# ============================    lista prenotazioni ricevimento   ========================== #
@student.route('/lista_prenotazioni_ricevimento')
class ListaPrenotazioniRIcevimento(Resource):
    @student.expect(freshman_student)
    @student.marshal_with(get_prenotazioni_ricevimento_model)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('matricola_studente', type=str, help='matricola_studente')
        args = parser.parse_args(strict=True)
        return reperimento_prenotazioni_ricevimento_studente(args['matricola_studente'], database.get_connection()), 201


# ============================    studente    ========================== #
@student.route('/login')
class Login(Resource):

    @student.expect(login_student_model)
    @student.marshal_with(student_model)
    def post(self):

        # arguments
        parser = reqparse.RequestParser()
        parser.add_argument('matricola_studente', type=str, help='matricola dello studente universitario')
        parser.add_argument('password_studente', type=str, help='password dello studente universitario')
        args = parser.parse_args(strict=True)

        return loginStudent(args['matricola_studente'], args['password_studente'], database.get_connection()), 250


# ============================    update password    ========================== #
@student.route('/password')
class Password(Resource):

    @student.expect(update_password_student_model)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nuova_password_studente', type=str, help='nuova password dello studente universitario')
        parser.add_argument('matricola_studente', type=str, help='matricola dello studente universitario')
        parser.add_argument('password_studente', type=str, help='password dello studente universitario')
        args = parser.parse_args(strict=True)

        updatePassword(args['nuova_password_studente'],
                       args['matricola_studente'],
                       args['password_studente'],
                       database.get_connection())


# ============================    get discipline   ========================== #
@student.route('/discipline')
class Discipline(Resource):

    def post(self):
        return {'riceve disciplina': '1'}


# ============================    segui disciplina   ========================== #
@student.route('/follow_disciplina')
class FollowDiscipline(Resource):

    @student.expect(follow_discipline_model)
    @student.marshal_with(follow_discipline_model)
    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument('codice_corso', type=str, help='codice del corso di laurea universitario')
        parser.add_argument('codice_disciplina', type=str, help='codice della disciplina universitaria')
        parser.add_argument('matricola_studente', type=str, help='codice della matricola studente universitaria')
        args = parser.parse_args(strict=True)

        followDiscipline(args['codice_corso'],
                         args['codice_disciplina'],
                         args['matricola_studente'],
                         database.get_connection())

        return args, 250


# ============================    unfollow disciplina   ========================== #
@student.route('/unfollow_disciplina')
class UnfollowDiscipline(Resource):

    @student.expect(follow_discipline_model)
    @student.marshal_with(follow_discipline_model)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('codice_corso', type=str, help='codice del corso di laurea universitario')
        parser.add_argument('codice_disciplina', type=str, help='codice della disciplina universitaria')
        parser.add_argument('matricola_studente', type=str, help='codice della matricola studente universitaria')
        args = parser.parse_args(strict=True)

        unFollowDiscipline(args['codice_corso'],
                           args['codice_disciplina'],
                           args['matricola_studente'],
                           database.get_connection())

        return args, 250


# ============================    calendario   ========================== #
@student.route('/calendario')
class Calendario(Resource):

    @student.expect(get_calendar_student_model)
    @student.marshal_with(calendar_model)
    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument('matricola_studente', type=str, help='codice della matricola studente universitaria')
        args = parser.parse_args(strict=True)

        return getCalendar(args['matricola_studente'], database.get_connection())


# ============================ reperimento contatti docenti  ========================== #
@student.route('/reperimento_lista_docenti_iscrizione_corso_piu_newsletter_per_chat')
class ListaDocentiPerChat(Resource):
    @student.expect(freshman_student)
    @student.marshal_with(lista_docenti_iscritti_corso_piu_newsletter_per_chat_model)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('matricola_studente', type=str, help='mat of student')
        args = parser.parse_args(strict=True)
        return reperimentoInfoDocentiCorsiENewsletter(args['matricola_studente'], database.get_connection()), 201


# ============================    lista ricevimenti prenotabili   ========================== #
@student.route('/lista_ricevimenti_prenotabili')
class ListaRicevimentoPrenotabile(Resource):
    @student.expect(freshman_student)
    @student.marshal_with(lista_ricevimenti_prenotabili_model)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('matricola_studente', type=str, help='matricola_studente')
        args = parser.parse_args(strict=True)
        return reperimento_ricevimenti_prenotabili(args['matricola_studente'], database.get_connection()), 201
