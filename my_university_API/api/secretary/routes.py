# This file contain all routes of secretary

####################################################################
#                             import
####################################################################
from api.secretary import secretary  # to use api
from flask_restx import Resource, reqparse, fields  # to use Resource, that expose http request method
from api.secretary.models import (insert_student_model,  # to import models
                                  insert_headoffice_model,
                                  get_head_office_model,
                                  insert_contact_model)
from api.secretary.query import (insertStudent,  # to import query of db
                                 insertHeadOffice,
                                 get_all_offices,
                                 insertHeadOfficeContact)
from api.database_config import DatabaseConnector

####################################################################
#                             object
####################################################################
# instance of the database connection
connection = DatabaseConnector('localhost', 'my_university_db', 'root', '').get_connection()


####################################################################
#                             routing
####################################################################

# ============================    sede    ========================== #
@secretary.route('/sede')
class HeadOffice(Resource):

    @secretary.marshal_with(get_head_office_model)
    def get(self):
        print('dentro get')
        cacca = get_all_offices(connection)
        print(cacca)
        return cacca, 250

    @secretary.expect(insert_headoffice_model)
    @secretary.marshal_with(insert_headoffice_model)
    def post(self):
        # arguments
        parser = reqparse.RequestParser()
        parser.add_argument('nome_sede', type=str, help='nome della sede universitaria')
        parser.add_argument('orario_apertura', type=int, help='orario apertura della sede universitaria')
        parser.add_argument('orario_chiusura', type=int, help='orario chiusura della sede universitaria')
        parser.add_argument('numero_piani', type=int, help='numero piani della sede universitaria')
        parser.add_argument('cap', type=int, help='cap della sede universitaria')
        parser.add_argument('via_piazza', type=str, help='cap della sede universitaria')
        parser.add_argument('civico', type=str, help='civico della sede universitaria')
        args = parser.parse_args(strict=True)

        insertHeadOffice(args['nome_sede'],
                         args['orario_apertura'],
                         args['orario_chiusura'],
                         args['numero_piani'],
                         args['cap'],
                         args['via_piazza'],
                         args['civico'],
                         connection)

        return args, 250


# ============================    aggiungi contatto  ========================== #
@secretary.route('/contatto_sede')
class Contact(Resource):

    @secretary.expect(insert_contact_model)
    @secretary.marshal_with(insert_contact_model)
    def post(self):
        # arguments
        parser = reqparse.RequestParser()
        parser.add_argument('nome_sede', type=str, help='nome della sede universitaria')
        parser.add_argument('tipo_contatto', type=str, help='tipo contatto della sede universitaria')
        parser.add_argument('valore_contatto', type=str, help='valore contatto della sede universitaria')
        args = parser.parse_args(strict=True)

        insertHeadOfficeContact(args['nome_sede'], args['tipo_contatto'], args['valore_contatto'], connection)

        return args, 250

# ============================    cancella sede    ========================== #
@secretary.route('/cancella_sede')
class DelHeadOffice(Resource):
    def post(self):
        return {'sede': '1'}


# ============================    aula    ========================== #
@secretary.route('/aula')
class Room(Resource):

    def post(self):
        return {'aula': '1'}


# ============================   cancella aula    ========================== #
@secretary.route('/cancella_aula')
class DelRoom(Resource):

    def post(self):
        return {'aula': '1'}


# ============================    corso laurea    ========================== #
@secretary.route('/corso_laurea')
class DegreeCourse(Resource):

    def get(self):
        return {'corso laurea': '1'}

    def post(self):
        return {'corso laurea': '2'}


# ============================    cancella corso laurea    ========================== #
@secretary.route('/cancella_corso_laurea')
class DelDegreeCourse(Resource):

    def post(self):
        return {'corso laurea': '1'}


# ============================    locazione    ========================== #
@secretary.route('/locazione')
class Located(Resource):

    def get(self):
        return {'locazione': '1'}

    def post(self):
        return {'locazione': '2'}


# ============================    cancella locazione    ========================== #
@secretary.route('/cancella_locazione')
class DelLocated(Resource):

    def post(self):
        return {'locazione': '1'}


# ============================    disciplina    ========================== #
@secretary.route('/disciplina')
class Discipline(Resource):

    def get(self):
        return {'disciplina': '1'}

    def post(self):
        return {'disciplina': '2'}


# ============================    cancella disciplina    ========================== #
@secretary.route('/cancella_disciplina')
class DelDiscipline(Resource):

    def post(self):
        return {'disciplina': '1'}


# ============================    docente    ========================== #
@secretary.route('/docente')
class Professor(Resource):

    def get(self):
        return {'docente': '1'}

    def post(self):
        return {'docente': '2'}


# ============================    cancella docente    ========================== #
@secretary.route('/cancella_docente')
class DelProfessor(Resource):

    def post(self):
        return {'docente': '1'}


# ============================    assunzione    ========================== #
@secretary.route('/assunzione')
class Assumption(Resource):

    def get(self):
        return {'assunzione': '1'}

    def post(self):
        return {'assunzione': '2'}


# ============================    studente    ========================== #
@secretary.route('/studente')
class Student(Resource):

    def get(self):
        return {'studente': '1'}

    @secretary.expect(insert_student_model)
    @secretary.marshal_with(insert_student_model)
    def post(self):

        # arguments
        parser = reqparse.RequestParser()
        parser.add_argument('cf', type=str, help='cf of student')
        parser.add_argument('nome', type=str, help='first name of student')
        parser.add_argument('cognome', type=str, help='last name of student')
        parser.add_argument('data_di_nascita', type=str, help='bd of student')
        parser.add_argument('luogo_di_nascita', type=str, help='cf of student')
        parser.add_argument('cap', type=str, help='first name of student')
        parser.add_argument('via_piazza', type=str, help='last name of student')
        parser.add_argument('civico', type=str, help='bd of student')
        parser.add_argument('matricola_studente', type=str, help='bd of student')
        parser.add_argument('email_studente', type=str, help='cf of student')
        parser.add_argument('data_immatricolazione', type=str, help='first name of student')
        parser.add_argument('password_studente', type=str, help='bd of student')
        args = parser.parse_args(strict=True)

        insertStudent(args['cf'],
                      args['nome'],
                      args['cognome'],
                      args['data_di_nascita'],
                      args['luogo_di_nascita'],
                      args['cap'],
                      args['via_piazza'],
                      args['civico'],
                      args['matricola_studente'],
                      args['email_studente'],
                      args['data_immatricolazione'],
                      args['password_studente'],
                      connection)

        return args, 201


# ============================   cancella studente    ========================== #
@secretary.route('/cancella_studente')
class DelStudent(Resource):

    def post(self):
        return {'studente': '2'}


# ============================    insegnamento    ========================== #
@secretary.route('/insegnamento')
class Teaching(Resource):

    def get(self):
        return {'insegnamento': '1'}

    def post(self):
        return {'insegnamento': '2'}


# ============================    cancella insegnamento    ========================== #
@secretary.route('/cancella_insegnamento')
class DelTeaching(Resource):

    def post(self):
        return {'insegnamento': '1'}


