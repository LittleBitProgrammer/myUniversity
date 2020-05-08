# This file contain all query of the database, of the secretary

####################################################################
#                             import
####################################################################
from mysql.connector import Error


####################################################################
#                             query
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

        mySQL_query_insert_head_office = """INSERT INTO sede(nome_sede,
                                                               orario_apertura,
                                                               orario_chiusura,
                                                               numero_piani,
                                                               cap,
                                                               via_piazza,
                                                               civico)
                                             VALUES(%s, %s, %s, %s, %s, %s, %s)"""

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
def get_all_offices(connection):
    head_offices = []

    try:
        cursor = connection.cursor(dictionary=True)
        mySQL_query_get_all_head_offices = """SELECT nome_sede,
                                                     orario_apertura,
                                                     orario_chiusura, 
                                                     numero_piani,
                                                     cap, 
                                                     via_piazza, 
                                                     civico
                                                     FROM sede"""

        mySQL_query_get_all_contact = """SELECT tipo_contatto, valore_contatto 
                                                         FROM contatto_sede
                                                         WHERE nome_sede = %s"""

        cursor.execute(mySQL_query_get_all_head_offices)
        head_offices = cursor.fetchall()

        for head_office in head_offices:
            print(head_office['nome_sede'])
            cursor.execute(mySQL_query_get_all_contact, (head_office['nome_sede'],))
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

        mySQL_query_insert_contact = """INSERT INTO contatto(tipo_contatto,valore_contatto)
                                        VALUES(%s,%s)"""
        mySQL_query_insert_head_office_contact = """INSERT INTO contatto_sede(nome_sede, tipo_contatto, valore_contatto)
                                                    VALUES(%s,%s,%s)"""

        contact_tuple = (tipo_contatto, valore_contatto)
        head_office_contact_tuple = (nome_sede, tipo_contatto, valore_contatto)

        print('BEFORE')
        cursor.execute(mySQL_query_insert_contact, contact_tuple)
        print('next is head office contact')
        cursor.execute(mySQL_query_insert_head_office_contact, head_office_contact_tuple)
        print('AFTER')
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

        mySQL_query_delete_head_office_contact = """DELETE FROM contatto_sede 
                                                    WHERE nome_sede = %s"""
        mySQL_query_delete_head_office_location = """DELETE FROM ospitazione 
                                                     WHERE nome_sede = %s"""
        mySQL_query_delete_head_office_room = """DELETE FROM aula 
                                                WHERE nome_sede = %s"""
        mySQL_query_delete_head_office_lesson = """DELETE FROM lezione 
                                                   WHERE nome_sede = %s"""
        mySQL_query_delete_head_office = """DELETE FROM sede 
                                            WHERE nome_sede = %s"""

        print(nome_sede)
        head_office_tuple = (nome_sede,)
        print(head_office_tuple)

        cursor.execute(mySQL_query_delete_head_office_contact, head_office_tuple)
        print('dopo contatto_sede')
        cursor.execute(mySQL_query_delete_head_office_location, head_office_tuple)
        print('dopo location')
        cursor.execute(mySQL_query_delete_head_office_lesson, head_office_tuple)
        print('dopo lezione')
        cursor.execute(mySQL_query_delete_head_office_room, head_office_tuple)
        print('dopo _aula')
        cursor.execute(mySQL_query_delete_head_office, head_office_tuple)
        print('dopo sede')

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
        mySQL_query_insert_room = """INSERT INTO aula(nome_sede, 
                                                      numero_piano, 
                                                      numero_aula, 
                                                      capienza)
                                     VALUES (%s, %s, %s, %s)"""

        room_tuple = (nome_sede, numero_piano, numero_aula, capienza)
        cursor.execute(mySQL_query_insert_room, room_tuple)

        connection.commit()
    except Error as error:
        print('failed to insert into mySQL table {error}')
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
        mySQL_query_delete_room_lesson = """DELETE FROM lezione
                                            WHERE nome_sede = %s
                                            AND numero_piano = %s 
                                            AND numero_aula = %s
                                           """
        mySQL_query_delete_room = """DELETE FROM aula
                                      WHERE nome_sede = %s
                                      AND numero_piano = %s
                                      AND numero_aula = %s"""

        delete_room_tuple = (nome_sede, numero_piano, numero_aula)
        cursor.execute(mySQL_query_delete_room_lesson, delete_room_tuple)
        cursor.execute(mySQL_query_delete_room, delete_room_tuple)

        connection.commit()
    except Error as error:
        print('failed to insert into mySQL table {error}')
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print('MySQL connection is closed')


# function to insert degree course inside database
def insertDegreeCourse(codice_corso, nome_corso, durata_corso_laurea, connection):
    try:
        cursor = connection.cursor()
        mySQL_query_insert_degree_course = """INSERT INTO corso_di_laurea (codice_corso, nome_corso, durata_corso_laurea) 
                                              VALUES (%s, %s, %s)"""

        degree_course_tuple = (codice_corso, nome_corso, durata_corso_laurea)

        cursor.execute(mySQL_query_insert_degree_course, degree_course_tuple)
        connection.commit()

    except Error as error:
        print('failed to insert into mySQL table {error}')
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
        mySQL_query_get_all_degree_courses = """SELECT codice_corso,
                                                     nome_corso,
                                                     durata_corso_laurea
                                               FROM corso_di_laurea"""

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

        mySQL_query_delete_location = """DELETE FROM ospitazione
                                         WHERE codice_corso = %s"""
        mySQL_query_delete_is_in = """DELETE FROM appartiene
                                      WHERE codice_corso = %s"""
        mySQL_query_delete_work = """DELETE FROM lavora
                                     WHERE codice_corso = %s"""
        mySQL_query_delete_lesson = """DELETE FROM lezione
                                       WHERE codice_corso = %s"""
        mySQL_query_delete_discipline = """DELETE FROM disciplina
                                           WHERE codice_corso = %s"""
        mySQL_query_delete_alert = """DELETE FROM avviso
                                      WHERE codice_corso = %s"""
        mySQL_query_delete_teaching = """DELETE FROM insegna
                                         WHERE codice_corso = %s"""
        mySQL_query_delete_followed_discipline = """DELETE FROM disciplina_seguita
                                                    WHERE codice_corso = %s"""
        mySQL_query_delete_newletter_subscription = """DELETE FROM iscrizione_newsletter
                                                        WHERE codice_corso = %s"""
        mySQL_query_delete_degree_course = """DELETE FROM corso_di_laurea
                                              WHERE codice_corso = %s"""

        delete_degree_course_tuple = (codice_corso,)

        cursor.execute(mySQL_query_delete_location, delete_degree_course_tuple)
        cursor.execute(mySQL_query_delete_is_in, delete_degree_course_tuple)
        cursor.execute(mySQL_query_delete_work, delete_degree_course_tuple)
        cursor.execute(mySQL_query_delete_lesson, delete_degree_course_tuple)
        cursor.execute(mySQL_query_delete_alert, delete_degree_course_tuple)
        cursor.execute(mySQL_query_delete_teaching, delete_degree_course_tuple)
        cursor.execute(mySQL_query_delete_followed_discipline, delete_degree_course_tuple)
        cursor.execute(mySQL_query_delete_newletter_subscription, delete_degree_course_tuple)
        cursor.execute(mySQL_query_delete_discipline, delete_degree_course_tuple)
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
        mySQL_query_insert_degree_course = """INSERT INTO ospitazione (nome_sede, codice_corso) 
                                              VALUES (%s, %s)"""

        degree_course_tuple = (nome_sede, codice_corso)

        cursor.execute(mySQL_query_insert_degree_course, degree_course_tuple)
        connection.commit()

    except Error as error:
        print('failed to insert into mySQL table {error}')
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
        mySQL_query_get_all_locations = """SELECT  corso_di_laurea.codice_corso, 
                                                   corso_di_laurea.nome_corso, 
                                                   corso_di_laurea.durata_corso_laurea,
                                                   sede.nome_sede, 
                                                   sede.orario_apertura,
                                                   sede.orario_chiusura,
                                                   sede.numero_piani,
                                                   sede.cap,
                                                   sede.via_piazza,
                                                   sede.civico
                                           FROM corso_di_laurea 
                                           NATURAL JOIN ospitazione
                                           NATURAL JOIN sede"""

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
        mySQL_query_delete_location = """DELETE FROM ospitazione
                                            WHERE nome_sede = %s
                                            AND codice_corso = %s"""

        delete_location_tuple = (nome_sede, codice_corso)
        cursor.execute(mySQL_query_delete_location, delete_location_tuple)

        connection.commit()
    except Error as error:
        print('failed to insert into mySQL table {error}')
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
    print('prima del try')
    try:
        print('dentro il try')
        cursor = connection.cursor()
        print('prima di query')
        mySQL_query_insert_discipline = """INSERT INTO disciplina(codice_corso, 
                                                                   codice_disciplina, 
                                                                   nome_disciplina, 
                                                                   cfu,
                                                                   semestre,
                                                                   anno)
                                        VALUES (%s, %s, %s, %s, %s, %s)"""

        print('dopo di query')
        discipline_tuple = (codice_corso, codice_disciplina, nome_disciplina, cfu, semestre, anno)

        print('dopo tupla')

        print(discipline_tuple)

        cursor.execute(mySQL_query_insert_discipline, discipline_tuple)
        print('dopo ex')
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
        mySQL_query_get_all_discipline = """SELECT corso_di_laurea.nome_corso, 
                                            disciplina.nome_disciplina, 
                                            disciplina.codice_disciplina, 
                                            disciplina.cfu,disciplina.anno, 
                                            disciplina.semestre 
                                            FROM corso_di_laurea 
                                            NATURAL JOIN disciplina 
                                            ORDER BY corso_di_laurea.nome_corso ASC"""

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

        mySQL_query_delete_lesson = """DELETE FROM lezione
                                       WHERE codice_corso = %s
                                       AND codice_disciplina = %s"""
        mySQL_query_delete_alert = """DELETE FROM avviso
                                      WHERE codice_corso = %s
                                      AND codice_disciplina = %s"""
        mySQL_query_delete_teaching = """DELETE FROM insegna
                                      WHERE codice_corso = %s
                                      AND codice_disciplina = %s"""
        mySQL_query_delete_followed_discipline = """DELETE FROM disciplina_seguita
                                                    WHERE codice_corso = %s
                                                    AND codice_disciplina = %s"""
        mySQL_query_delete_newletter_subscription = """DELETE FROM iscrizione_newsletter
                                                       WHERE codice_corso = %s
                                                       AND codice_disciplina = %s"""
        mySQL_query_delete_discipline = """DELETE FROM disciplina
                                          WHERE codice_corso = %s
                                          AND codice_disciplina = %s"""

        delete_degree_course_tuple = (codice_corso, codice_disciplina)

        cursor.execute(mySQL_query_delete_lesson, delete_degree_course_tuple)
        cursor.execute(mySQL_query_delete_alert, delete_degree_course_tuple)
        cursor.execute(mySQL_query_delete_teaching, delete_degree_course_tuple)
        cursor.execute(mySQL_query_delete_followed_discipline, delete_degree_course_tuple)
        cursor.execute(mySQL_query_delete_newletter_subscription, delete_degree_course_tuple)
        cursor.execute(mySQL_query_delete_discipline, delete_degree_course_tuple)

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

        # query persona
        mySql_insert_person = """INSERT INTO persona(cf, 
                                                       nome,
                                                       cognome, 
                                                       data_di_nascita,
                                                       luogo_di_nascita,
                                                       cap,
                                                       via_piazza,
                                                       civico)  
                                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s) """

        # student query
        mySql_insert_teacher = """INSERT INTO docente(matricola_docente, 
                                                       cf,
                                                       email_docente,
                                                       password_docente) 
                                    VALUES (%s, %s, %s, %s) """

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
        mySQL_query_get_all_teachers = """SELECT docente.matricola_docente, 
                                                   persona.nome,
                                                   persona.cognome,
                                                   docente.email_docente,
                                                   docente.cf,
                                                   persona.data_di_nascita,
                                                   persona.luogo_di_nascita,
                                                   persona.cap,
                                                   persona.via_piazza,
                                                   persona.civico
                                             FROM docente
                                             NATURAL JOIN persona"""

        mySQL_query_get_all_contact = """SELECT tipo_contatto, valore_contatto 
                                         FROM contatto_persona 
                                         WHERE cf = %s"""

        cursor.execute(mySQL_query_get_all_teachers)
        teachers = cursor.fetchall()

        for teacher in teachers:
            cursor.execute(mySQL_query_get_all_contact, (teacher['cf'],))
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

        mySQL_query_delete_teacher_contacts = """DELETE FROM contatto_persona
                                                 WHERE cf = %s"""
        mySQL_query_delete_teacher_person = """DELETE FROM persona
                                               WHERE cf = %s"""
        mySQL_query_delete_teacher_teach = """DELETE FROM insegna
                                              WHERE matricola_docente = %s"""
        mySQL_query_delete_teacher_alert = """DELETE FROM avviso
                                              WHERE matricola_docente = %s"""
        mySQL_query_delete_teacher_receipt = """DELETE FROM ricevimento
                                                WHERE matricola_docente = %s"""
        mySQL_query_delete_teacher = """DELETE FROM docente
                                        WHERE matricola_docente = %s"""
        mySQL_query_delete_contact = """DELETE FROM contatto
                                        WHERE tipo_contatto = %s
                                        AND  valore_contatto = %s"""
        mySQL_query_select_contact = """SELECT tipo_contatto, valore_contatto
                                        FROM contatto_persona
                                        WHERE cf = %s"""
        mySQL_query_delete_teacher_receipt_request = """DELETE FROM richiesta_ricevimento
                                                        WHERE matricola_docente = %s"""

        delete_teacher_tuple = (matricola_docente,)

        cursor.execute(mySQL_query_delete_teacher_alert, delete_teacher_tuple)  # 1
        cursor.execute(mySQL_query_delete_teacher_teach, delete_teacher_tuple)  # 2
        cursor.execute(mySQL_query_delete_teacher_receipt_request, delete_teacher_tuple)  # 3
        cursor.execute(mySQL_query_delete_teacher_receipt, delete_teacher_tuple)  # 4
        cursor.execute(mySQL_query_select_contact, (cf,))  # 5

        contacts = cursor.fetchall()
        print(contacts)

        cursor.execute(mySQL_query_delete_teacher_contacts, (cf,))  # 5

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
        mySql_insert_studente = """INSERT INTO studente(matricola_studente, 
                                                       cf,
                                                       email_studente,
                                                       data_immatricolazione,
                                                       password_studente) 
                                    VALUES (%s, %s, %s, %s, %s) """

        # is in query
        mySql_insert_is_in = """INSERT INTO appartiene(codice_corso,
                                                       matricola_studente) 
                                            VALUES (%s, %s)"""

        # tuple of person and student
        person_tuple = (cf, nome, cognome, data_di_nascita, luogo_di_nascita, cap, via_piazza, civico)
        student_tuple = (matricola_studente, cf, email_studente, data_immatricolazione, password_studente)
        is_in_tuple = (codice_corso, matricola_studente)

        cursor.execute(mySql_insert_persona, person_tuple)
        cursor.execute(mySql_insert_studente, student_tuple)
        cursor.execute(mySql_insert_is_in, is_in_tuple)

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
        mySQL_query_get_all_students = """SELECT studente.matricola_studente, 
                                                   persona.nome,
                                                   persona.cognome,
                                                   studente.email_studente,
                                                   studente.data_immatricolazione,
                                                   studente.cf,
                                                   persona.data_di_nascita,
                                                   persona.luogo_di_nascita,
                                                   persona.cap,
                                                   persona.via_piazza,
                                                   persona.civico
                                             FROM studente
                                             NATURAL JOIN persona"""

        mySQL_query_get_all_contact = """SELECT tipo_contatto, valore_contatto 
                                         FROM contatto_persona 
                                         WHERE cf = %s"""

        cursor.execute(mySQL_query_get_all_students)
        students = cursor.fetchall()
        print(students)

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

        mySQL_query_delete_teach = """DELETE FROM insegna
                                      WHERE matricola_docente = %s
                                      AND codice_corso = %s
                                      AND codice_disciplina = %s"""

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

        mySQL_query_insert_teach = """INSERT INTO insegna(matricola_docente, codice_corso, codice_disciplina) 
                                           VALUES (%s, %s, %s)"""

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

        mySQL_query_delete_teacher_contacts = """DELETE FROM contatto_persona
                                                 WHERE cf = %s"""
        mySQL_query_delete_student_person = """DELETE FROM persona
                                               WHERE cf = %s"""
        mySQL_query_delete_student = """DELETE FROM studente
                                         WHERE matricola_studente = %s"""
        mySQL_query_delete_contact = """DELETE FROM contatto
                                        WHERE tipo_contatto = %s
                                        AND  valore_contatto = %s"""
        mySQL_query_select_contact = """SELECT tipo_contatto, valore_contatto
                                        FROM contatto_persona
                                        WHERE cf = %s"""
        mySQL_query_delete_student_receipt_request = """DELETE FROM richiesta_ricevimento
                                                        WHERE matricola_studente = %s"""
        mySQL_query_delete_student_newsletter = """DELETE FROM iscrizione_newsletter 
                                                   WHERE matricola_studente = %s"""
        mySQL_query_delete_student_followed_discipline = """DELETE FROM disciplina_seguita 
                                                            WHERE matricola_studente = %s"""
        mySQL_query_delete_student_is_in = """DELETE FROM appartiene 
                                                   WHERE matricola_studente = %s"""

        delete_student_tuple = (matricola_studente,)

        cursor.execute(mySQL_query_delete_student_is_in, delete_student_tuple)
        cursor.execute(mySQL_query_select_contact, (cf,))

        contacts = cursor.fetchall()
        cursor.execute(mySQL_query_delete_teacher_contacts, (cf,))

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
        mySQL_query_get_all_teachings = """SELECT docente.matricola_docente, 
                                                  persona.nome, 
                                                  persona.cognome, 
                                                  docente.email_docente, 
                                                  corso_di_laurea.nome_corso, 
                                                  disciplina.codice_disciplina, 
                                                  disciplina.nome_disciplina, 
                                                  disciplina.cfu, 
                                                  disciplina.anno, 
                                                  disciplina.semestre, 
                                                  sede.nome_sede,
                                                  sede.via_piazza,
                                                  sede.civico,
                                                  sede.orario_apertura,
                                                  sede.orario_chiusura
                                            FROM persona 
                                            INNER JOIN docente ON persona.cf = docente.cf
                                            INNER JOIN insegna ON docente.matricola_docente = insegna.matricola_docente
                                            INNER JOIN disciplina ON insegna.codice_corso = disciplina.codice_corso and insegna.codice_disciplina = disciplina.codice_disciplina
                                            INNER JOIN corso_di_laurea ON disciplina.codice_corso = corso_di_laurea.codice_corso
                                            INNER JOIN ospitazione ON corso_di_laurea.codice_corso = ospitazione.codice_corso
                                            INNER JOIN sede ON ospitazione.nome_sede = sede.nome_sede
                                            ORDER BY docente.matricola_docente ASC"""

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
