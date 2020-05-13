# This file contain all database functions of the secretary

####################################################################
#                             import
####################################################################
from mysql.connector import Error  # to use error
from api.student.query import (mySQL_query_login_studente,
                               mysql_query_get_student_contacts,
                               mysql_query_update_password)


####################################################################
#                             DB_functions
####################################################################

# function tomlogin the studente
def loginStudent(matricola_studente, password_studente, connection):
    students = []

    try:
        cursor = connection.cursor()

        student_tuple = (matricola_studente, password_studente)
        cursor = connection.cursor(dictionary=True)
        cursor.execute(mySQL_query_login_studente, student_tuple)
        students = cursor.fetchall()

        for temp_student in students:
            cursor.execute(mysql_query_get_student_contacts, (temp_student['cf'],))
            temp_student['contatti'] = cursor.fetchall()

    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")
            return students


# function to update student password
def updatePassword(nuova_password_studente, matricola_studente, password_studente, connection):
    try:
        cursor = connection.cursor()

        student_tuple = (nuova_password_studente, matricola_studente, password_studente)
        cursor = connection.cursor(dictionary=True)
        cursor.execute(mysql_query_update_password, student_tuple)
        connection.commit()
        print("Password Updated!")
    except Error as error:
        print(f"Error from MySQL: {error}")
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")
