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

    def post(self):
        return {'studente': '2'}


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


# ============================    lezione    ========================== #
@secretary.route('/lezione')
class Lesson(Resource):

    def post(self):
        return {'lezione': '2'}


# ============================   cancella lezione    ========================== #
@secretary.route('/cancella_lezione')
class DelLesson(Resource):

    def post(self):
        return {'lezione': '1'}
