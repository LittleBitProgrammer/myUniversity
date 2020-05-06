from mysql.connector import Error

def loginProfessor(matricola_docente, password_docente, connection):
    records = []

    try:

        cursor = connection.cursor()

        sql_select_Query = """SELECT persona.cf,
                                     persona.nome,
                                     persona.cognome, 
                                     persona.data_di_nascita, 
                                     persona.luogo_di_nascita, 
                                     persona.cap, 
                                     persona.via_piazza, 
                                     persona.civico, 
                                     docente.matricola_docente,
                                     docente.email_docente
                                FROM persona INNER JOIN docente 
                                ON persona.cf = docente.cf 
                                WHERE docente.matricola_docente = %s
                                AND docente.password_docente = %s"""

        professor_tuple = (matricola_docente, password_docente)

        cursor = connection.cursor(dictionary=True)
        cursor.execute(sql_select_Query, professor_tuple)
        records = cursor.fetchall()

        print(records)

        mysql_query_contacts = """SELECT tipo_contatto, valore_contatto
                                          FROM contatto_persona
                                          WHERE cf = %s"""

        record_tuple = (records[0]['cf'],)
        cursor.execute(mysql_query_contacts, record_tuple)
        contacts = cursor.fetchall()

        print(contacts)

        records[0]['contatti'] = contacts

        print("Fetching each row using column name")

    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()
            print("MySQL connection is closed")
            return records

def updatePassword(nuova_password_docente, matricola_docente, password_docente , connection):
    try:
        cursor = connection.cursor()
        sql_update_password_Query = """ UPDATE docente 
                                        SET password_docente = %s 
                                        WHERE (matricola_docente = %s AND password_docente = %s)"""

        professor_tuple = (nuova_password_docente, matricola_docente, password_docente)

        cursor = connection.cursor(dictionary=True)
        cursor.execute(sql_update_password_Query, professor_tuple)
        connection.commit()
        print("Password Updated!")
    except Error as e:
        print("Error from MySQL", e)
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()
            print("MySQL connection is closed")
