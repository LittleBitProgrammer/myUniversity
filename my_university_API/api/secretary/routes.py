# This file contain all routes of secretary

####################################################################
#                             import
####################################################################
from api.secretary import secretary  # to use api
from flask_restx import Resource, reqparse, fields  # to use Resource, that expose http request method
from api.secretary.models import *
import mysql.connector
from mysql.connector import Error


####################################################################
#                             function
####################################################################
def insertStudent(cf,
                  nome,
                  cognome,
                  data_di_nascita,
                  luogo_di_nascita,
                  cap,
                  via_piazza,
                  civico,
                  matricola_studente,
                  email_studente,
                  data_immatricolazione,
                  password_studente
                  ):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='my_university_db',
                                             user='root',
                                             password='')
        cursor = connection.cursor()
        print(cf,
               nome,
               cognome,
               data_di_nascita,
               luogo_di_nascita,
               cap,
               via_piazza,
               civico)
        # query persona
        mySql_insert_persona = """INSERT INTO persona(cf, 
                                                       nome,
                                                       cognome, 
                                                       data_di_nascita,
                                                       luogo_di_nascita,
                                                       cap,
                                                       via_piazza,
                                                       civico)  
                                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s) """

        # student query
        mySql_insert_studente = """ INSERT INTO studente(matricola_studente, 
                                                       cf,
                                                       email_studente,
                                                       data_immatricolazione,
                                                       password_studente) 
                                    VALUES (%s, %s, %s, %s, %s) """

        # tuple of person and student
        person_tuple = (cf, nome, cognome, data_di_nascita, luogo_di_nascita, cap, via_piazza, civico)
        student_tuple = (matricola_studente, cf, email_studente, data_immatricolazione, password_studente)

        cursor.execute(mySql_insert_persona, person_tuple)
        cursor.execute(mySql_insert_studente, student_tuple)

        connection.commit()
        print("Record inserted successfully into Person and Student table")
    except Error as error:
        print(f"Failed to insert into MySQL table {error}")
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


####################################################################
#                             routing
####################################################################

# ============================    sede    ========================== #
@secretary.route('/sede')
class HeadOffice(Resource):

    def get(self):
        return {'sede': '1'}

    def post(self):
        return {'sede': '2'}


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

    @secretary.expect(student_model)
    @secretary.marshal_with(student_model)
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
                      args['password_studente'])

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


