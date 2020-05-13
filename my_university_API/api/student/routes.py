# This file contain all routes of student (This file is for Roberto)

####################################################################
#                             import
####################################################################
from api.student import student  # to use api
from flask_restx import Resource, reqparse, fields  # to use Resource, that expose http request method
from api.database_config import DatabaseConnector
from api.student.database_functions import (loginStudent,
                                            updatePassword,
                                            followDiscipline,
                                            unFollowDiscipline,
                                            getCalendar)

from api.student.models import (student_model,
                                login_student_model,
                                update_password_student_model,
                                follow_discipline_model,
                                calendar_model,
                                get_calendar_student_model)


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
                         connection.get_connection())

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
                           connection.get_connection())

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

        return getCalendar(args['matricola_studente'], connection.get_connection())
