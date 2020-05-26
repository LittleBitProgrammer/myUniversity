# This file contain all routes of secretary

####################################################################
#                             import
####################################################################
from flask_restx import Resource, reqparse  # to use Resource, that expose http request method
from api.secretary.database_functions import *
from api.secretary.models import *
from api.database_config import DatabaseConnector

####################################################################
#                             object
####################################################################
# instance of the database connection
connection = DatabaseConnector('localhost', 'my_university_db', 'root', '')


####################################################################
#                             routing
####################################################################

# ============================    sede    ========================== #
@secretary.route('/sede')
class HeadOffice(Resource):

    @secretary.marshal_with(get_head_office_model)
    def get(self):
        print(get_all_head_offices(connection.get_connection()))
        return get_all_head_offices(connection.get_connection()), 250

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
                         connection.get_connection())

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

        insertHeadOfficeContact(args['nome_sede'],
                                args['tipo_contatto'],
                                args['valore_contatto'],
                                connection.get_connection())

        return args, 250


# ============================    cancella sede    ========================== #
@secretary.route('/cancella_sede')
class DelHeadOffice(Resource):
    @secretary.expect(delete_head_office_model)
    @secretary.marshal_with(delete_head_office_model)
    def post(self):
        # arguments
        parser = reqparse.RequestParser()
        parser.add_argument('nome_sede', type=str, help='nome della sede universitaria')
        args = parser.parse_args(strict=True)

        deleteHeadOffice(args['nome_sede'], connection.get_connection())
        return args, 250


# ============================    aula    ========================== #
@secretary.route('/aula')
class Room(Resource):

    @secretary.expect(insert_room_model)
    @secretary.marshal_with(insert_room_model)
    def post(self):
        # arguments
        parser = reqparse.RequestParser()
        parser.add_argument('nome_sede', type=str, help='nome della sede universitaria')
        parser.add_argument('numero_piano', type=int, help='numero piano dell\' aula universitaria')
        parser.add_argument('numero_aula', type=int, help='numero aula universitaria')
        parser.add_argument('capienza', type=int, help='capienza dell\' aula universitaria')
        args = parser.parse_args(strict=True)

        insertRoom(args['nome_sede'],
                   args['numero_piano'],
                   args['numero_aula'],
                   args['capienza'],
                   connection.get_connection())

        return args, 250


# ============================   cancella aula    ========================== #
@secretary.route('/cancella_aula')
class DelRoom(Resource):

    @secretary.expect(delete_room_model)
    @secretary.marshal_with(delete_room_model)
    def post(self):
        # arguments
        parser = reqparse.RequestParser()
        parser.add_argument('nome_sede', type=str, help='nome della sede universitaria')
        parser.add_argument('numero_piano', type=int, help='numero piano dell\' aula universitaria')
        parser.add_argument('numero_aula', type=int, help='numero aula universitaria')
        args = parser.parse_args(strict=True)

        deleteRoom(args['nome_sede'],
                   args['numero_piano'],
                   args['numero_aula'],
                   connection.get_connection())

        return args, 250


# ============================    corso laurea    ========================== #
@secretary.route('/corso_laurea')
class DegreeCourse(Resource):

    @secretary.marshal_with(insert_degree_course_model)
    def get(self):
        return get_all_degree_courses(connection.get_connection()), 250

    @secretary.expect(insert_degree_course_model)
    @secretary.marshal_with(insert_degree_course_model)
    def post(self):
        # arguments
        parser = reqparse.RequestParser()
        parser.add_argument('codice_corso', type=str, help='codice corso universitario')
        parser.add_argument('nome_corso', type=str, help='nome corso universitario')
        parser.add_argument('durata_corso_laurea', type=int, help='durata corso laurea universitario')
        args = parser.parse_args(strict=True)

        insertDegreeCourse(args['codice_corso'],
                           args['nome_corso'],
                           args['durata_corso_laurea'],
                           connection.get_connection())
        return args, 250


# ============================    cancella corso laurea    ========================== #
@secretary.route('/cancella_corso_laurea')
class DelDegreeCourse(Resource):

    @secretary.expect(delete_degree_course_model)
    @secretary.marshal_with(delete_degree_course_model)
    def post(self):
        # arguments
        parser = reqparse.RequestParser()
        parser.add_argument('codice_corso', type=str, help='codice corso universitario')
        args = parser.parse_args(strict=True)

        deleteDegreeCourse(args['codice_corso'], connection.get_connection())
        return args, 250


# ============================    locazione    ========================== #
@secretary.route('/locazione')
class Located(Resource):

    @secretary.marshal_with(get_all_location_model)
    def get(self):
        return get_all_locations(connection.get_connection()), 250

    @secretary.expect(insert_location_model)
    @secretary.marshal_with(insert_location_model)
    def post(self):
        # arguments
        parser = reqparse.RequestParser()
        parser.add_argument('nome_sede', type=str, help='nome sede universitaria')
        parser.add_argument('codice_corso', type=str, help='codice corso universitario')
        args = parser.parse_args(strict=True)

        insertLocation(args['nome_sede'], args['codice_corso'], connection.get_connection())
        return args, 250


# ============================    cancella locazione    ========================== #
@secretary.route('/cancella_locazione')
class DelLocated(Resource):

    @secretary.expect(insert_location_model)
    @secretary.marshal_with(insert_location_model)
    def post(self):
        # arguments
        parser = reqparse.RequestParser()
        parser.add_argument('nome_sede', type=str, help='nome sede universitaria')
        parser.add_argument('codice_corso', type=str, help='codice corso universitario')
        args = parser.parse_args(strict=True)

        deleteLocation(args['nome_sede'], args['codice_corso'], connection.get_connection())
        return args, 250


# ============================    disciplina    ========================== #
@secretary.route('/disciplina')
class Discipline(Resource):

    @secretary.marshal_with(get_all_discipline_model)
    def get(self):
        return get_all_discipline(connection.get_connection())

    @secretary.expect(insert_discipline_model)
    @secretary.marshal_with(insert_discipline_model)
    def post(self):
        # arguments
        parser = reqparse.RequestParser()
        parser.add_argument('codice_corso', type=str, help='codice corso universitario')
        parser.add_argument('codice_disciplina', type=str, help='codice della disciplina universitaria')
        parser.add_argument('nome_disciplina', type=str, help='nome della disciplina universitaria')
        parser.add_argument('cfu', type=int, help='numero di cfu della disciplina universitaria')
        parser.add_argument('semestre', type=int, help='semestre della disciplina universitaria')
        parser.add_argument('anno', type=int, help='anna della disciplina universitaria')
        args = parser.parse_args(strict=True)

        insertDiscipline(args['codice_corso'],
                         args['codice_disciplina'],
                         args['nome_disciplina'],
                         args['cfu'],
                         args['semestre'],
                         args['anno'],
                         connection.get_connection())

        return args, 250


# ============================    cancella disciplina    ========================== #
@secretary.route('/cancella_disciplina')
class DelDiscipline(Resource):

    @secretary.expect(delete_discipline_model)
    @secretary.marshal_with(delete_discipline_model)
    def post(self):
        # arguments
        parser = reqparse.RequestParser()
        parser.add_argument('codice_corso', type=str, help='codice corso universitario')
        parser.add_argument('codice_disciplina', type=str, help='codice disciplina universitaria')
        args = parser.parse_args(strict=True)

        deleteDiscipline(args['codice_corso'], args['codice_disciplina'], connection.get_connection())
        return args, 250


# ============================    docente    ========================== #
@secretary.route('/docente')
class Professor(Resource):

    @secretary.marshal_with(get_all_teacher_model)
    def get(self):
        # print(get_all_teachers(connection.get_connection()))
        return get_all_teachers(connection.get_connection()), 250

    @secretary.expect(insert_teacher_model)
    @secretary.marshal_with(insert_teacher_model)
    def post(self):
        # arguments
        parser = reqparse.RequestParser()
        parser.add_argument('cf', type=str, help='cf del docente')
        parser.add_argument('nome', type=str, help='nome del docente')
        parser.add_argument('cognome', type=str, help='cognome del docente')
        parser.add_argument('data_di_nascita', type=str, help='data di nascita del docente')
        parser.add_argument('luogo_di_nascita', type=str, help='luogo di nascita del docente')
        parser.add_argument('cap', type=int, help='cap del docente')
        parser.add_argument('via_piazza', type=str, help='indirizzo del docente')
        parser.add_argument('civico', type=str, help='civico del docente')
        parser.add_argument('matricola_docente', type=str, help='matricola del docente')
        parser.add_argument('email_docente', type=str, help='email del docente')
        parser.add_argument('password_docente', type=str, help='password del docente')
        args = parser.parse_args(strict=True)

        insertTeacher(args['cf'],
                      args['nome'],
                      args['cognome'],
                      args['data_di_nascita'],
                      args['luogo_di_nascita'],
                      args['cap'],
                      args['via_piazza'],
                      args['civico'],
                      args['matricola_docente'],
                      args['email_docente'],
                      args['password_docente'],
                      connection.get_connection())

        return args, 250


# ============================    cancella docente    ========================== #
@secretary.route('/cancella_docente')
class DelProfessor(Resource):

    @secretary.expect(delete_teacher_model)
    @secretary.marshal_with(delete_teacher_model)
    def post(self):
        # arguments
        parser = reqparse.RequestParser()
        parser.add_argument('cf', type=str, help='cf del docente')
        parser.add_argument('matricola_docente', type=str, help='matricola del docente')
        args = parser.parse_args(strict=True)

        deleteTeacher(args['cf'], args['matricola_docente'], connection.get_connection())
        return args, 250


# ============================    studente    ========================== #
@secretary.route('/studente')
class Student(Resource):

    @secretary.marshal_with(get_all_student_model)
    def get(self):
        return get_all_students(connection.get_connection())

    @secretary.expect(insert_student_model)
    @secretary.marshal_with(insert_student_model)
    def post(self):
        # arguments
        parser = reqparse.RequestParser()
        parser.add_argument('cf', type=str, help='cf dello studente')
        parser.add_argument('nome', type=str, help='nome dello studente')
        parser.add_argument('cognome', type=str, help='cognome dello studente')
        parser.add_argument('data_di_nascita', type=str, help='data di nascita dello studente')
        parser.add_argument('luogo_di_nascita', type=str, help='luogo di nascita dello studente')
        parser.add_argument('cap', type=str, help='cap dello studente')
        parser.add_argument('via_piazza', type=str, help='via piazza dello studente')
        parser.add_argument('civico', type=str, help='civico dello studente')
        parser.add_argument('matricola_studente', type=str, help='matricola studente dello studente')
        parser.add_argument('email_studente', type=str, help='email dello studente')
        parser.add_argument('data_immatricolazione', type=str, help='data immatricolazione dello studente')
        parser.add_argument('password_studente', type=str, help='password dello studente')
        parser.add_argument('codice_corso', type=str, help='codice del corso di laurea universitario')
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
                      args['codice_corso'],
                      connection.get_connection())

        return args, 201


# ============================   cancella studente    ========================== #
@secretary.route('/cancella_studente')
class DelStudent(Resource):

    @secretary.expect(delete_student_model)
    @secretary.marshal_with(delete_student_model)
    def post(self):
        # arguments
        parser = reqparse.RequestParser()
        parser.add_argument('cf', type=str, help='cf dello studente')
        parser.add_argument('matricola_studente', type=str, help='matricola studente universitario')
        args = parser.parse_args(strict=True)

        deleteStudent(args['cf'], args['matricola_studente'], connection.get_connection())
        return args, 250


# ============================    insegnamento    ========================== #
@secretary.route('/insegnamento')
class Teaching(Resource):

    @secretary.marshal_with(get_all_teachings_model)
    def get(self):
        return get_all_teachings(connection.get_connection()), 250

    @secretary.expect(delete_teach_model)
    @secretary.marshal_with(delete_teach_model)
    def post(self):
        # arguments
        parser = reqparse.RequestParser()
        parser.add_argument('matricola_docente', type=str, help='matricola del docente')
        parser.add_argument('codice_corso', type=str, help='codice del corso di laurea universitario')
        parser.add_argument('codice_disciplina', type=str, help='codice della disciplina universitaria')
        args = parser.parse_args(strict=True)

        insertTeach(args['matricola_docente'],
                    args['codice_corso'],
                    args['codice_disciplina'],
                    connection.get_connection())

        return args, 250


# ============================    cancella insegnamento    ========================== #
@secretary.route('/cancella_insegnamento')
class DelTeaching(Resource):

    @secretary.expect(delete_teach_model)
    @secretary.marshal_with(delete_teach_model)
    def post(self):
        # arguments
        parser = reqparse.RequestParser()
        parser.add_argument('matricola_docente', type=str, help='matricola del docente')
        parser.add_argument('codice_corso', type=str, help='codice del corso di laurea universitario')
        parser.add_argument('codice_disciplina', type=str, help='codice della disciplina universitaria')
        args = parser.parse_args(strict=True)

        deleteTeach(args['matricola_docente'],
                    args['codice_corso'],
                    args['codice_disciplina'],
                    connection.get_connection())
        return args, 250


# =================
@secretary.route('/aggiorna_anno_in_corso')
class UpdateYearStudent(Resource):

    @secretary.expect(update_anno_in_corso_studente_model)
    @secretary.marshal_with(update_anno_in_corso_studente_model)
    def post(self):
        # arguments
        parser = reqparse.RequestParser()
        parser.add_argument('anno_in_corso', type=str, help='anno in corso dello studente')
        parser.add_argument('matricola_studente', type=str, help='matricola studente universitario')
        args = parser.parse_args(strict=True)

        updateAnnoInCorso(args['anno_in_corso'], args['matricola_studente'], connection.get_connection())
        return args, 250

# ============================    lavora    ========================== #
@secretary.route('/lavora')
class Room(Resource):

    @secretary.expect(insert_lavora_model)
    def post(self):
        # arguments
        parser = reqparse.RequestParser()
        parser.add_argument('codice_corso', type=str, help='codice del corso di laurea')
        parser.add_argument('matricola_docente', type=int, help='matricola del docente')
        args = parser.parse_args(strict=True)

        insertLavora(args['codice_corso'],
                   args['matricola_docente'],
                   connection.get_connection())
        return args, 250