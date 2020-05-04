# This file contain all routes of secretary

####################################################################
#                             import
####################################################################
from api.secretary import secretary  # to use api
from flask_restx import Resource  # to use Resource, that expose http request method


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

    def delete(self):
        return {'sede': '3'}


# ============================    aula    ========================== #
@secretary.route('/aula')
class Room(Resource):

    def post(self):
        return {'aula': '2'}

    def delete(self):
        return {'aula': '3'}


# ============================    corso laurea    ========================== #
@secretary.route('/corso_laurea')
class DegreeCourse(Resource):

    def get(self):
        return {'corso laurea': '1'}

    def post(self):
        return {'corso laurea': '2'}

    def delete(self):
        return {'corso laurea': '3'}


# ============================    locazione    ========================== #
@secretary.route('/locazione')
class Located(Resource):

    def get(self):
        return {'locazione': '1'}

    def post(self):
        return {'locazione': '2'}

    def delete(self):
        return {'locazione': '3'}


# ============================    disciplina    ========================== #
@secretary.route('/disciplina')
class Discipline(Resource):

    def get(self):
        return {'disciplina': '1'}

    def post(self):
        return {'disciplina': '2'}

    def delete(self):
        return {'disciplina': '3'}


# ============================    docente    ========================== #
@secretary.route('/docente')
class Professor(Resource):

    def get(self):
        return {'docente': '1'}

    def post(self):
        return {'docente': '2'}

    def delete(self):
        return {'docente': '3'}


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

    def post(self):
        return {'studente': '2'}

    def delete(self):
        return {'studente': '3'}


# ============================    insegnamento    ========================== #
@secretary.route('/insegnamento')
class Teaching(Resource):

    def get(self):
        return {'insegnamento': '1'}

    def post(self):
        return {'insegnamento': '2'}

    def delete(self):
        return {'insegnamento': '3'}


# ============================    lezione    ========================== #
@secretary.route('/lezione')
class Teaching(Resource):

    def post(self):
        return {'lezione': '2'}

    def delete(self):
        return {'lezione': '3'}