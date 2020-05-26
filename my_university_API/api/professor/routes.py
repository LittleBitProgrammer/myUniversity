# This file contain all routes of professor

####################################################################
#                             import
####################################################################

from flask_restx import Resource, reqparse, fields  # to use Resource, that expose http request method
from api.professor.database_functions import *
from api.professor.models import *
from api.database_config import DatabaseConnector

database = DatabaseConnector('localhost', 'my_university_db', 'root', '')


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

        return loginProfessor(args['matricola_docente'], args['password_docente'], database.get_connection()), 201

# ============================    password    ========================== #
@professor.route('/update_password')
class UpdatePassword(Resource):
    @professor.expect(update_password_professor)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nuova_password_docente', type=str, help='mat of professor')
        parser.add_argument('matricola_docente', type=str, help='mat of professor')
        parser.add_argument('password_docente', type=str, help='mat of professor')
        args = parser.parse_args(strict=True)
        updatePassword(args['nuova_password_docente'], args['matricola_docente'], args['password_docente'], database.get_connection())


# ============================    insegnamento    ========================== #
@professor.route('/reperimento_insegnamenti')
class Teaching(Resource):
    @professor.expect(freshman_professor)
    @professor.marshal_with(get_teachings_professor)
    def post(self):
        # arguments
        parser = reqparse.RequestParser()
        parser.add_argument('matricola_docente', type=str, help='mat of professor')
        args = parser.parse_args(strict=True)
        return reperimento_insegnamenti_docente(args['matricola_docente'], database.get_connection()), 201


# ============================    post lezione    ========================== #
@professor.route('/inserimento_lezione')
class InsertLesson(Resource):
    @professor.expect(insert_lesson_model)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('codice_corso', type=str, help='codice_corso')
        parser.add_argument('codice_disciplina', type=str, help='codice_disciplina')
        parser.add_argument('nome_sede', type=str, help='nome_sede')
        parser.add_argument('numero_piano', type=str, help='numero_piano')
        parser.add_argument('numero_aula', type=str, help='numero_aula')
        parser.add_argument('numero_lezione', type=str, help='numero_lezione')
        parser.add_argument('data_inizio', type=str, help='data_inizio')
        parser.add_argument('numero_ore', type=str, help='numero_ore')
        parser.add_argument('titolo', type=str, help='titolo')
        parser.add_argument('descrizione', type=str, help='descrizione')
        args = parser.parse_args(strict=True)
        inserimento_lezione_docente(args['codice_corso'], args['codice_disciplina'], args['nome_sede'],
                                    args['numero_piano'], args['numero_aula'], args['numero_lezione'],
                                    args['data_inizio'], args['numero_ore'], args['titolo'],
                                    args['descrizione'], database.get_connection())


# ============================    cancella lezione    ========================== #
@professor.route('/cancella_lezione')
class DelLesson(Resource):
    @professor.expect(delete_lesson_model)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('codice_corso', type=str, help='codice_corso')
        parser.add_argument('codice_disciplina', type=str, help='codice_disciplina')
        parser.add_argument('nome_sede', type=str, help='nome_sede')
        parser.add_argument('numero_piano', type=str, help='numero_piano')
        parser.add_argument('numero_aula', type=str, help='numero_aula')
        parser.add_argument('numero_lezione', type=str, help='numero_lezione')
        args = parser.parse_args(strict=True)
        eliminazione_lezione_docente(args['codice_corso'], args['codice_disciplina'], args['nome_sede'],
                                    args['numero_piano'], args['numero_aula'], args['numero_lezione'],database.get_connection())


# ============================   get lezioni    ========================== #
@professor.route('/reperimento_lezioni')
class GetLessons(Resource):
    @professor.expect(freshman_professor)
    @professor.marshal_with(get_lessons_model)
    def post(self):
        # arguments
        parser = reqparse.RequestParser()
        parser.add_argument('matricola_docente', type=str, help='mat of professor')
        args = parser.parse_args(strict=True)
        return reperimento_lezione_docente(args['matricola_docente'], database.get_connection()), 201


# ============================  avviso   ========================== #
@professor.route('/inserimento_avviso')
class Alert(Resource):
    @professor.expect(insert_avviso_model)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('matricola_docente', type=str, help='mat of professor')
        parser.add_argument('codice_corso', type=str, help='codice_corso')
        parser.add_argument('codice_disciplina', type=str, help='codice_disciplina')
        parser.add_argument('data_avviso', type=str, help='data_inizio')
        parser.add_argument('titolo_avviso', type=str, help='titolo')
        parser.add_argument('corpo_avviso', type=str, help='descrizione')
        args = parser.parse_args(strict=True)
        inserimento_avviso_docente(args['matricola_docente'],
                                   args['codice_corso'],
                                   args['codice_disciplina'],
                                   args['data_avviso'],
                                   args['titolo_avviso'],
                                   args['corpo_avviso'],
                                   database.get_connection())


# ============================  avvisi   ========================== #
@professor.route('/reperimento_avvisi')
class GetAlerts(Resource):
    @professor.expect(freshman_professor)
    @professor.marshal_with(reperimento_avvisi_model)
    def post(self):
        # arguments
        parser = reqparse.RequestParser()
        parser.add_argument('matricola_docente', type=str, help='mat of professor')
        args = parser.parse_args(strict=True)
        return reperimento_avvisi_docente(args['matricola_docente'], database.get_connection()), 201


# ============================  ricevimento   ========================== #
@professor.route('/inserimento_ricevimento')
class InsertReceipt(Resource):
    @professor.expect(insert_ricevimento_model)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('matricola_docente', type=str, help='mat of professor')
        parser.add_argument('data_ricevimento', type=str, help='data_ricevimento')
        parser.add_argument('ore_ricevimento', type=str, help='ore_ricevimento')
        args = parser.parse_args(strict=True)
        inserimento_ricevimento(args['matricola_docente'], args['data_ricevimento'], args['ore_ricevimento'], database.get_connection())


# ============================  update ricevimento   ========================== #
@professor.route('/aggiorna_richiesta_ricevimento')
class UpdateRichiestaRicevimento(Resource):
    @professor.expect(update_richiesta_ricevimento_model)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('matricola_docente', type=str, help='matricola_docente')
        parser.add_argument('data_ricevimento', type=str, help='data_ricevimento')
        parser.add_argument('matricola_studente', type=str, help='matricola_studente')
        parser.add_argument('ora_inizio', type=str, help='ora_inizio')
        parser.add_argument('durata', type=str, help='durata')
        args = parser.parse_args(strict=True)
        update_richiesta_ricevimento(args['matricola_docente'],
                                     args['data_ricevimento'],
                                     args['matricola_studente'],
                                     args['ora_inizio'],
                                     args['durata'],
                                     database.get_connection())




# ============================  cancella ricevimento   ========================== #
@professor.route('/cancella_ricevimento')
class DelReceipt(Resource):
    @professor.expect(delete_ricevimento_model)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('matricola_docente', type=str, help='mat of professor')
        parser.add_argument('data_ricevimento', type=str, help='data_ricevimento')
        args = parser.parse_args(strict=True)
        delete_ricevimento(args['matricola_docente'],
                           args['data_ricevimento'],
                           database.get_connection())


# ============================ richiesta ricevimento   ========================== #
@professor.route('/reperimento_ricevimenti')
class Receipts(Resource):
    @professor.expect(freshman_professor)
    @professor.marshal_with(reperimento_ricevimenti_info)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('matricola_docente', type=str, help='mat of professor')
        args = parser.parse_args(strict=True)
        return reperimento_info_ricevimenti(args['matricola_docente'], database.get_connection()), 201

# ============================ reperimento contatti studenti  ========================== #
@professor.route('/reperimento_lista_studenti_iscritti_corso_piu_newsletter_per_chat')
class Receipts(Resource):
    @professor.expect(freshman_professor)
    @professor.marshal_with(lista_studenti_iscritti_corso_piu_newsletter_per_chat_model)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('matricola_docente', type=str, help='mat of professor')
        args = parser.parse_args(strict=True)
        return reperimentoInfoStudentiCorsiENewsletter(args['matricola_docente'], database.get_connection()), 201
