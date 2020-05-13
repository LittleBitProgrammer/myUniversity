# This file contain all database functions of the secretary

####################################################################
#                             import
####################################################################
from mysql.connector import Error  # to use error
from api.student.query import (mySQL_query_login_studente,
                               mySQL_query_get_student_contacts,
                               mySQL_query_update_password,
                               mySQL_query_follow_discipline,
                               mySQL_query_delete_follow_discipline,
                               mySQL_query_get_calendar)


####################################################################
#                             DB_functions
####################################################################

# function to login the studente
def loginStudent(matricola_studente, password_studente, connection):
    students = []

    try:
        cursor = connection.cursor()

        student_tuple = (matricola_studente, password_studente)
        cursor = connection.cursor(dictionary=True)
        cursor.execute(mySQL_query_login_studente, student_tuple)
        students = cursor.fetchall()

        for temp_student in students:
            cursor.execute(mySQL_query_get_student_contacts, (temp_student['cf'],))
            temp_student['contatti'] = cursor.fetchall()

    except Error as e:
        print('Error reading data from MySQL table', e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print('MySQL connection is closed')
            return students


# function to update student password
def updatePassword(nuova_password_studente, matricola_studente, password_studente, connection):
    try:

        student_tuple = (nuova_password_studente, matricola_studente, password_studente)
        cursor = connection.cursor(dictionary=True)
        cursor.execute(mySQL_query_update_password, student_tuple)
        connection.commit()

        print('Password Updated!')
    except Error as error:
        print(f'Error from MySQL: {error}')
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print('MySQL connection is closed')


# function to follow a discipline
def followDiscipline(codice_corso, codice_disciplina, matricola_studente, connection):
    try:
        cursor = connection.cursor(dictionary=True)

        follow_discipline_tuple = (codice_corso, codice_disciplina, matricola_studente)
        cursor.execute(mySQL_query_follow_discipline, follow_discipline_tuple)
        connection.commit()
        print('Discipline followed')
    except Error as error:
        print(f"Error from mySQL: {error}")
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print('MySQL connection is closed')


# function to unfollow discipline
def unFollowDiscipline(codice_corso, codice_disciplina, matricola_studente, connection):
    try:
        cursor = connection.cursor(dictionary=True)

        unFollow_discipline_tuple = (codice_corso, codice_disciplina, matricola_studente)
        cursor.execute(mySQL_query_delete_follow_discipline, unFollow_discipline_tuple)
        connection.commit()

        print('Discipline unfollowed')
    except Error as error:
        print(f"Error from mySQL: {error}")
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print('MySQL connection is closed')


# function to get student calendar
def getCalendar(matricola_studente, connection):

    lessons = []
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(mySQL_query_get_calendar, (matricola_studente,))
        lessons = cursor.fetchall()
    except Error as error:
        print(f"Error from mySQL: {error}")
    finally:
        if connection.is_connected():
            print('cacca')
            connection.close()
            cursor.close()
            print('MySQL connection is closed')
            return lessons
