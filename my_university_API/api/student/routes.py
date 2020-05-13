# This file contain all routes of student (This file is for Roberto)

####################################################################
#                             import
####################################################################
from api.student import student  # to use api
from flask_restx import Resource, reqparse, fields  # to use Resource, that expose http request method
from api.database_config import DatabaseConnector
from api.student.database_functions import (loginStudent,
                                            updatePassword)
from api.student.models import (student_model,
                                login_student_model,
                                update_password_student_model)


####################################################################
#                             object
####################################################################
# instance of the database connection
connection = DatabaseConnector('localhost', 'my_university_db', 'root', '')


####################################################################
#                             routing
####################################################################
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

        return loginStudent(args['matricola_studente'], args['password_studente'], connection.get_connection()), 250


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
                       connection.get_connection())


# ============================    get contatto   ========================== #
@student.route('/contatti')
class GetContact(Resource):

    def post(self):
        return {'contatti': '1'}


# ============================    get discipline   ========================== #
@student.route('/discipline')
class Discipline(Resource):

    def post(self):
        return {'riceve disciplina': '1'}


# ============================    segui disciplina   ========================== #
@student.route('/follow_disciplina')
class FollowDiscipline(Resource):

    def post(self):
        return {'segui disciplina': '1'}


# ============================    unfollow disciplina   ========================== #
@student.route('/unfollow_disciplina')
class UnfollowDiscipline(Resource):

    def post(self):
        return {'segui disciplina': '1'}


# ============================    calendario   ========================== #
@student.route('/calendario')
class Calendario(Resource):

    def post(self):
        return {'iscrizione newsletter': '1'}
