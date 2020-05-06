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
        print(head_office_tuple)
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
                  password_studente
                  ):
    try:
        connection = database.get_connection()
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