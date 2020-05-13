# This file contain all database functions of the secretary

####################################################################
#                             import
####################################################################
from mysql.connector import Error  # to use error
from api.secretary.query import (mySQL_query_insert_head_office,
                                 mySQL_query_get_all_head_offices,
                                 mySQL_query_get_all_head_office_contacts,
                                 mySQL_query_insert_contact,
                                 mySQL_query_insert_head_office_contact,
                                 mySQL_query_delete_head_office,
                                 mySQL_query_delete_head_office_contact,
                                 mySQL_query_delete_head_office_lesson,
                                 mySQL_query_delete_head_office_location,
                                 mySQL_query_delete_head_office_room,
                                 mySQL_query_insert_room,
                                 mySQL_query_delete_room_lesson,
                                 mySQL_query_delete_room,
                                 mySQL_query_insert_degree_course,
                                 mySQL_query_get_all_degree_courses,
                                 mySQL_query_delete_degree_course_alert,
                                 mySQL_query_delete_degree_course,
                                 mySQL_query_delete_degree_course_discipline,
                                 mySQL_query_delete_degree_course_followed_discipline,
                                 mySQL_query_delete_degree_course_is_in,
                                 mySQL_query_delete_degree_course_lesson,
                                 mySQL_query_delete_degree_course_location,
                                 mySQL_query_delete_degree_course_newletter_subscription,
                                 mySQL_query_delete_degree_course_teaching,
                                 mySQL_query_delete_degree_course_work,
                                 mySQL_query_insert_location,
                                 mySQL_query_get_all_locations,
                                 mySQL_query_delete_location,
                                 mySQL_query_insert_discipline,
                                 mySQL_query_get_all_discipline,
                                 mySQL_query_delete_discipline_alert,
                                 mySQL_query_delete_discipline,
                                 mySQL_query_delete_discipline_followed_discipline,
                                 mySQL_query_delete_discipline_lesson,
                                 mySQL_query_delete_discipline_newletter_subscription,
                                 mySQL_query_delete_discipline_teaching,
                                 mySql_insert_person,
                                 mySql_insert_teacher,
                                 mySQL_query_get_all_person_contacts,
                                 mySQL_query_get_all_teachers,
                                 mySQL_query_delete_contact,
                                 mySQL_query_delete_teacher,
                                 mySQL_query_delete_teacher_alert,
                                 mySQL_query_delete_person_contacts,
                                 mySQL_query_delete_teacher_person,
                                 mySQL_query_delete_teacher_receipt,
                                 mySQL_query_delete_teacher_receipt_request,
                                 mySQL_query_delete_teacher_teach,
                                 mySQL_query_select_contact,
                                 mySql_insert_student_is_in,
                                 mySql_insert_student,
                                 mySQL_query_get_all_contact,
                                 mySQL_query_get_all_students,
                                 mySQL_query_delete_teach,
                                 mySQL_query_insert_teach,
                                 mySQL_query_delete_student,
                                 mySQL_query_delete_student_followed_discipline,
                                 mySQL_query_delete_student_is_in,
                                 mySQL_query_delete_student_newsletter,
                                 mySQL_query_delete_student_person,
                                 mySQL_query_delete_student_receipt_request,
                                 mySQL_query_get_all_teachings)


####################################################################
#                             DB_functions
####################################################################

####################################################################
#                             Convenzioni:
#   Per le POST
#       def *operazione**Nometabella* (*input*, connection):
#
#   Per le GET
#       def get_all_*nome_tabella* (*input*, connection):
####################################################################

# function to insert head office inside database
def insertHeadOffice(nome_sede,
                     orario_apertura,
                     orario_chiusura,
                     numero_piani,
                     cap,
                     via_piazza,
                     civico,
                     connection):
    try:
        cursor = connection.cursor()

        head_office_tuple = (nome_sede, orario_apertura, orario_chiusura, numero_piani, cap, via_piazza, civico)
        cursor.execute(mySQL_query_insert_head_office, head_office_tuple)
        connection.commit()

        print("Record inserted successfully into SEDE table")
    except Error as error:
        print(f"Failed to insert into MySQL table {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


# function to gets all head offices
def get_all_head_offices(connection):
    head_offices = []

    try:
        cursor = connection.cursor(dictionary=True)

        cursor.execute(mySQL_query_get_all_head_offices)
        head_offices = cursor.fetchall()

        for head_office in head_offices:
            cursor.execute(mySQL_query_get_all_head_office_contacts, (head_office['nome_sede'],))
            head_office['contatti'] = cursor.fetchall()

    except Error as error:
        print(f"Failed to insert into MySQL table {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            return head_offices


# function to insert contact of an head office
def insertHeadOfficeContact(nome_sede, tipo_contatto, valore_contatto, connection):
    try:
        cursor = connection.cursor()

        contact_tuple = (tipo_contatto, valore_contatto)
        head_office_contact_tuple = (nome_sede, tipo_contatto, valore_contatto)

        cursor.execute(mySQL_query_insert_contact, contact_tuple)
        cursor.execute(mySQL_query_insert_head_office_contact, head_office_contact_tuple)
        connection.commit()
    except Error as error:
        print(f"Failed to insert into MySQL table {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


# function to delete sede from database
def deleteHeadOffice(nome_sede, connection):
    try:
        cursor = connection.cursor()

        head_office_tuple = (nome_sede,)

        cursor.execute(mySQL_query_delete_head_office_contact, head_office_tuple)
        cursor.execute(mySQL_query_delete_head_office_location, head_office_tuple)
        cursor.execute(mySQL_query_delete_head_office_lesson, head_office_tuple)
        cursor.execute(mySQL_query_delete_head_office_room, head_office_tuple)
        cursor.execute(mySQL_query_delete_head_office, head_office_tuple)

        connection.commit()
        print("Record deleted successfully")
    except Error as error:
        print(f"Failed to insert into MySQL table {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


# function to insert a room
def insertRoom(nome_sede,
               numero_piano,
               numero_aula,
               capienza,
               connection):
    try:
        cursor = connection.cursor()

        room_tuple = (nome_sede, numero_piano, numero_aula, capienza)
        cursor.execute(mySQL_query_insert_room, room_tuple)

        connection.commit()
    except Error as error:
        print(f'failed to insert into mySQL table {error}')
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print('MySQL connection is closed')


# function to delete room inside database
def deleteRoom(nome_sede,
               numero_piano,
               numero_aula,
               connection):
    try:
        cursor = connection.cursor()

        delete_room_tuple = (nome_sede, numero_piano, numero_aula)
        cursor.execute(mySQL_query_delete_room_lesson, delete_room_tuple)
        cursor.execute(mySQL_query_delete_room, delete_room_tuple)

        connection.commit()
    except Error as error:
        print(f'failed to insert into mySQL table {error}')
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print('MySQL connection is closed')


# function to insert degree course inside database
def insertDegreeCourse(codice_corso, nome_corso, durata_corso_laurea, connection):
    try:
        cursor = connection.cursor()

        degree_course_tuple = (codice_corso, nome_corso, durata_corso_laurea)

        cursor.execute(mySQL_query_insert_degree_course, degree_course_tuple)
        connection.commit()

    except Error as error:
        print(f'failed to insert into mySQL table {error}')
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print('MySQL connection is closed')


# function to gets all degree course
def get_all_degree_courses(connection):
    degree_courses = []

    try:
        cursor = connection.cursor(dictionary=True)

        cursor.execute(mySQL_query_get_all_degree_courses)
        degree_courses = cursor.fetchall()

    except Error as error:
        print(f"Failed to insert into MySQL table {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            return degree_courses


# function to delete room inside database
def deleteDegreeCourse(codice_corso, connection):
    try:
        cursor = connection.cursor()

        delete_degree_course_tuple = (codice_corso,)

        cursor.execute(mySQL_query_delete_degree_course_location, delete_degree_course_tuple)
        cursor.execute(mySQL_query_delete_degree_course_is_in, delete_degree_course_tuple)
        cursor.execute(mySQL_query_delete_degree_course_work, delete_degree_course_tuple)
        cursor.execute(mySQL_query_delete_degree_course_lesson, delete_degree_course_tuple)
        cursor.execute(mySQL_query_delete_degree_course_alert, delete_degree_course_tuple)
        cursor.execute(mySQL_query_delete_degree_course_teaching, delete_degree_course_tuple)
        cursor.execute(mySQL_query_delete_degree_course_followed_discipline, delete_degree_course_tuple)
        cursor.execute(mySQL_query_delete_degree_course_newletter_subscription, delete_degree_course_tuple)
        cursor.execute(mySQL_query_delete_degree_course_discipline, delete_degree_course_tuple)
        cursor.execute(mySQL_query_delete_degree_course, delete_degree_course_tuple)

        connection.commit()
    except Error as error:
        print(f'failed to insert into mySQL table {error}')
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print('MySQL connection is closed')


# function to insert located course-head office inside database
def insertLocation(nome_sede, codice_corso, connection):
    try:
        cursor = connection.cursor()

        degree_course_tuple = (nome_sede, codice_corso)

        cursor.execute(mySQL_query_insert_location, degree_course_tuple)
        connection.commit()

    except Error as error:
        print(f'failed to insert into mySQL table {error}')
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print('MySQL connection is closed')


# function to gets all location head office- degree course
def get_all_locations(connection):
    locations = []

    try:
        cursor = connection.cursor(dictionary=True)

        cursor.execute(mySQL_query_get_all_locations)
        locations = cursor.fetchall()

    except Error as error:
        print(f"Failed to insert into MySQL table {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            return locations


# function to delete location inside database
def deleteLocation(nome_sede,
                   codice_corso,
                   connection):
    try:
        cursor = connection.cursor()

        delete_location_tuple = (nome_sede, codice_corso)
        cursor.execute(mySQL_query_delete_location, delete_location_tuple)

        connection.commit()
    except Error as error:
        print(f'failed to insert into mySQL table {error}')
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print('MySQL connection is closed')


def insertDiscipline(codice_corso,
                     codice_disciplina,
                     nome_disciplina,
                     cfu,
                     semestre,
                     anno,
                     connection):
    try:
        cursor = connection.cursor()

        discipline_tuple = (codice_corso, codice_disciplina, nome_disciplina, cfu, semestre, anno)

        cursor.execute(mySQL_query_insert_discipline, discipline_tuple)
        connection.commit()
    except Error as error:
        print(f'failed to insert into mySQL table {error}')
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print('MySQL connection is closed')


# function to gets all location head office- degree course
def get_all_discipline(connection):
    discipline = []

    try:
        cursor = connection.cursor(dictionary=True)

        cursor.execute(mySQL_query_get_all_discipline)
        discipline = cursor.fetchall()

    except Error as error:
        print(f"Failed to insert into MySQL table {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            return discipline


# function to delete discipline inside database
def deleteDiscipline(codice_corso, codice_disciplina, connection):
    try:
        cursor = connection.cursor()

        delete_discipline_tuple = (codice_corso, codice_disciplina)

        cursor.execute(mySQL_query_delete_discipline_lesson, delete_discipline_tuple)
        cursor.execute(mySQL_query_delete_discipline_alert, delete_discipline_tuple)
        cursor.execute(mySQL_query_delete_discipline_teaching, delete_discipline_tuple)
        cursor.execute(mySQL_query_delete_discipline_followed_discipline, delete_discipline_tuple)
        cursor.execute(mySQL_query_delete_discipline_newletter_subscription, delete_discipline_tuple)
        cursor.execute(mySQL_query_delete_discipline, delete_discipline_tuple)

        connection.commit()
    except Error as error:
        print(f'failed to insert into mySQL table {error}')
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print('MySQL connection is closed')


# function to insert teacher inside database
def insertTeacher(cf,
                  nome,
                  cognome,
                  data_di_nascita,
                  luogo_di_nascita,
                  cap,
                  via_piazza,
                  civico,
                  matricola_docente,
                  email_docente,
                  password_docente,
                  connection):
    try:
        cursor = connection.cursor()

        # tuple of person and student
        person_tuple = (cf, nome, cognome, data_di_nascita, luogo_di_nascita, cap, via_piazza, civico)
        teacher_tuple = (matricola_docente, cf, email_docente, password_docente)

        cursor.execute(mySql_insert_person, person_tuple)
        cursor.execute(mySql_insert_teacher, teacher_tuple)

        connection.commit()
        print("Record inserted successfully into Person and Student table")
    except Error as error:
        print(f"Failed to insert into MySQL table {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


# function to gets all teachers
def get_all_teachers(connection):
    teachers = []

    try:
        cursor = connection.cursor(dictionary=True)

        cursor.execute(mySQL_query_get_all_teachers)
        teachers = cursor.fetchall()

        for teacher in teachers:
            cursor.execute(mySQL_query_get_all_person_contacts, (teacher['cf'],))
            teacher['contatti'] = cursor.fetchall()

    except Error as error:
        print(f"Failed to insert into MySQL table {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            return teachers


# function to delete teacher inside database
def deleteTeacher(cf, matricola_docente, connection):
    try:

        cursor = connection.cursor(dictionary=True)

        delete_teacher_tuple = (matricola_docente,)

        cursor.execute(mySQL_query_delete_teacher_alert, delete_teacher_tuple)  # 1
        cursor.execute(mySQL_query_delete_teacher_teach, delete_teacher_tuple)  # 2
        cursor.execute(mySQL_query_delete_teacher_receipt_request, delete_teacher_tuple)  # 3
        cursor.execute(mySQL_query_delete_teacher_receipt, delete_teacher_tuple)  # 4
        cursor.execute(mySQL_query_select_contact, (cf,))  # 5

        contacts = cursor.fetchall()

        cursor.execute(mySQL_query_delete_person_contacts, (cf,))  # 5

        for contact in contacts:
            cursor.execute(mySQL_query_delete_contact, (contact['tipo_contatto'], contact['valore_contatto']))  # 7

        cursor.execute(mySQL_query_delete_teacher, delete_teacher_tuple)  # 8
        cursor.execute(mySQL_query_delete_teacher_person, (cf,))  # 9

        connection.commit()
    except Error as error:
        print(f'failed to insert into mySQL table {error}')
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print('MySQL connection is closed')


# function to insert student inside database
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
                  password_studente,
                  codice_corso,
                  connection):
    try:
        cursor = connection.cursor()

        # tuple of person and student
        person_tuple = (cf, nome, cognome, data_di_nascita, luogo_di_nascita, cap, via_piazza, civico)
        student_tuple = (matricola_studente, cf, email_studente, data_immatricolazione, password_studente)
        is_in_tuple = (codice_corso, matricola_studente)

        cursor.execute(mySql_insert_person, person_tuple)
        cursor.execute(mySql_insert_student, student_tuple)
        cursor.execute(mySql_insert_student_is_in, is_in_tuple)

        connection.commit()
        print("Record inserted successfully into Person and Student table")
    except Error as error:
        print(f"Failed to insert into MySQL table {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


# function to gets all students
def get_all_students(connection):
    students = []

    try:
        cursor = connection.cursor(dictionary=True)

        cursor.execute(mySQL_query_get_all_students)
        students = cursor.fetchall()

        for student in students:
            cursor.execute(mySQL_query_get_all_contact, (student['cf'],))
            student['contatti'] = cursor.fetchall()

    except Error as error:
        print(f"Failed to insert into MySQL table {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            return students


# function to delete teach inside database
def deleteTeach(matricola_docente, codice_corso, codice_disciplina, connection):
    try:

        cursor = connection.cursor(dictionary=True)

        delete_teach_tuple = (matricola_docente, codice_corso, codice_disciplina)

        cursor.execute(mySQL_query_delete_teach, delete_teach_tuple)  # 1

        connection.commit()
    except Error as error:
        print(f'failed to insert into mySQL table {error}')
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print('MySQL connection is closed')


def insertTeach(matricola_docente, codice_corso, codice_disciplina, connection):
    try:
        cursor = connection.cursor()

        teach_tuple = (matricola_docente, codice_corso, codice_disciplina)
        cursor.execute(mySQL_query_insert_teach, teach_tuple)

        connection.commit()
    except Error as error:
        print(f'failed to insert into mySQL table {error}')
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print('MySQL connection is closed')


# function to delete teacher inside database
def deleteStudent(cf, matricola_studente, connection):
    try:

        cursor = connection.cursor(dictionary=True)

        delete_student_tuple = (matricola_studente,)

        cursor.execute(mySQL_query_delete_student_is_in, delete_student_tuple)
        cursor.execute(mySQL_query_select_contact, (cf,))

        contacts = cursor.fetchall()
        cursor.execute(mySQL_query_delete_person_contacts, (cf,))

        for contact in contacts:
            cursor.execute(mySQL_query_delete_contact, (contact['tipo_contatto'], contact['valore_contatto']))  # 7

        cursor.execute(mySQL_query_delete_student_receipt_request, delete_student_tuple)
        cursor.execute(mySQL_query_delete_student_followed_discipline, delete_student_tuple)
        cursor.execute(mySQL_query_delete_student_newsletter, delete_student_tuple)

        cursor.execute(mySQL_query_delete_student, delete_student_tuple)  # 8
        cursor.execute(mySQL_query_delete_student_person, (cf,))  # 9

        connection.commit()
    except Error as error:
        print(f'failed to insert into mySQL table {error}')
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print('MySQL connection is closed')


# function to gets all teaching
def get_all_teachings(connection):
    teachings = []

    try:
        cursor = connection.cursor(dictionary=True)

        cursor.execute(mySQL_query_get_all_teachings)
        teachings = cursor.fetchall()

    except Error as error:
        print(f"Failed to insert into MySQL table {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            return teachings
