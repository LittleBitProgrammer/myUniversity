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
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


# function to gets all head offices
def get_all_offices(connection):
    head_offices = []

    try:
        cursor = connection.cursor(dictionary=True)
        mySQL_query_get_all_head_offices = """SELECT sede.nome_sede,
                                                     orario_apertura,
                                                     orario_chiusura, 
                                                     numero_piani, cap, 
                                                     via_piazza, civico, 
                                                     tipo_contatto, 
                                                     valore_contatto 
                                                     FROM sede 
                                                     LEFT JOIN contatto_sede 
                                                     ON sede.nome_sede = contatto_sede.nome_sede"""

        cursor.execute(mySQL_query_get_all_head_offices)
        head_offices = cursor.fetchall()

    except Error as error:
        print(f"Failed to insert into MySQL table {error}")
    finally:
        if (connection.is_connected()):
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
        if (connection.is_connected()):
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
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


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
                  connection ):
    try:
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