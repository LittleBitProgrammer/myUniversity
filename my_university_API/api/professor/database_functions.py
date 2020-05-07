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

def reperimento_insegnamenti_docente(matricola_docente, connection):
    records = []
    try:
        cursor = connection.cursor()
        sql_select_Query = """
        SELECT 
        matricola_docente, codice_corso, codice_disciplina,
        nome_disciplina, cfu, semestre, anno, 
        nome_corso, durata_corso_laurea,
        nome_sede,
        orario_apertura,orario_chiusura,numero_piani,cap,via_piazza,civico
        FROM insegna
        NATURAL JOIN disciplina
        NATURAL JOIN corso_di_laurea
        NATURAL JOIN ospitazione
        NATURAL JOIN sede
        WHERE matricola_docente = %s;"""
        professor_tuple = (matricola_docente,)
        cursor = connection.cursor(dictionary=True)
        cursor.execute(sql_select_Query, professor_tuple)
        records = cursor.fetchall()
        print(records)
        print("fetchall success!")
    except Error as e:
        print("Error reading data from MySQL tables", e)
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()
            print("MySQL connection is closed")
            return records

def inserimento_lezione_docente(codice_corso, codice_disciplina,
                                nome_sede, numero_piano, numero_aula,
                                numero_lezione, data_inizio, numero_ore,
                                titolo, descrizione, connection):
    try:
        cursor = connection.cursor()
        sql_insert_lesson_Query = """INSERT INTO lezione 
                                    (codice_corso, codice_disciplina, 
                                    nome_sede, numero_piano, 
                                    numero_aula, numero_lezione, 
                                    data_inizio, numero_ore, titolo, 
                                    descrizione) 
                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
        lesson_tuple = (codice_corso, codice_disciplina,
                        nome_sede, numero_piano, numero_aula,
                        numero_lezione, data_inizio, numero_ore,
                        titolo, descrizione)
        # print('codice_corso',codice_corso)
        # print('codice_disciplina', codice_disciplina)
        # print('nome_sede', nome_sede)
        # print('numero_piano', numero_piano)
        # print('numero_aula', numero_aula)
        # print('numero_lezione', numero_lezione)
        # print('data_inizio', data_inizio)
        # print('numero_ore', numero_ore)
        # print('titolo', titolo)
        # print('descrizione', descrizione)
        cursor = connection.cursor(dictionary=True)
        cursor.execute(sql_insert_lesson_Query, lesson_tuple)
        connection.commit()
        print("Record inserted successfully into Lezione table")
    except Error as error:
        print(f"Failed to insert into MySQL table {error}")
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def reperimento_lezione_docente(matricola_docente, connection):
    records = []
    try:
        cursor = connection.cursor()
        sql_select_Query = """SELECT nome_sede, numero_piano, cap, via_piazza, civico, 
                              numero_aula, codice_corso, nome_corso, codice_disciplina, 
                              nome_disciplina, cfu, anno, semestre, numero_lezione, 
                              data_inizio, numero_ore, titolo, descrizione, capienza 
                              FROM insegna 
                              NATURAL JOIN disciplina 
                              NATURAL JOIN lezione 
                              NATURAL JOIN corso_di_laurea
                              NATURAL JOIN aula 
                              NATURAL JOIN sede 
                              WHERE matricola_docente = %s ORDER BY data_inizio"""
        professor_tuple = (matricola_docente,)
        cursor = connection.cursor(dictionary=True)
        cursor.execute(sql_select_Query, professor_tuple)
        records = cursor.fetchall()
        print(records)
        print("Fetching each row")
    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()
            print("MySQL connection is closed")
            return records

def eliminazione_lezione_docente(codice_corso, codice_disciplina,
                                nome_sede, numero_piano, numero_aula,
                                numero_lezione, connection):
    try:
        cursor = connection.cursor()
        sql_insert_lesson_Query = """DELETE FROM lezione WHERE 
                                    codice_corso = %s AND 
                                    codice_disciplina = %s AND 
                                    nome_sede = %s AND 
                                    numero_piano = %s AND 
                                    numero_aula = %s AND 
                                    numero_lezione = %s;"""
        lesson_tuple = (codice_corso, codice_disciplina,
                        nome_sede, numero_piano, numero_aula,
                        numero_lezione)
        # print('codice_corso',codice_corso)
        # print('codice_disciplina', codice_disciplina)
        # print('nome_sede', nome_sede)
        # print('numero_piano', numero_piano)
        # print('numero_aula', numero_aula)
        # print('numero_lezione', numero_lezione)
        cursor = connection.cursor(dictionary=True)
        cursor.execute(sql_insert_lesson_Query, lesson_tuple)
        connection.commit()
        print("Record delete successfully into Lezione table")
    except Error as error:
        print(f"Failed to delete into MySQL table {error}")
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def inserimento_avviso_docente(matricola_docente,
                               codice_corso,
                               codice_disciplina,
                               data_avviso,
                               titolo_avviso,
                               corpo_avviso,
                               connection):
    try:
        cursor = connection.cursor()
        sql_insert_new_Query = """INSERT INTO avviso 
                                    (matricola_docente, 
                                    codice_corso, 
                                    codice_disciplina, 
                                    data_avviso, 
                                    titolo_avviso, 
                                    corpo_avviso) 
                                    VALUES (%s, %s, %s, %s, %s, %s);"""
        new_tuple = (matricola_docente, codice_corso, codice_disciplina,
                        data_avviso, titolo_avviso, corpo_avviso)
        # print('matricola_docente', matricola_docente)
        # print('codice_corso',codice_corso)
        # print('codice_disciplina', codice_disciplina)
        # print('data_avviso', data_avviso)
        # print('titolo_avviso', titolo_avviso)
        # print('corpo_avviso', corpo_avviso)
        cursor = connection.cursor(dictionary=True)
        cursor.execute(sql_insert_new_Query, new_tuple)
        connection.commit()
        print("Record inserted successfully into Avviso table")
    except Error as error:
        print(f"Failed to insert into MySQL table {error}")
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def reperimento_avvisi_docente(matricola_docente, connection):
    records = []
    try:
        cursor = connection.cursor()
        sql_select_Query = """
        SELECT codice_corso, codice_disciplina, 
        data_avviso, titolo_avviso, corpo_avviso, 
        nome_disciplina, semestre, anno 
        FROM avviso NATURAL JOIN disciplina 
        WHERE matricola_docente = %s 
        ORDER BY data_avviso DESC;"""
        professor_tuple = (matricola_docente,)
        cursor = connection.cursor(dictionary=True)
        cursor.execute(sql_select_Query, professor_tuple)
        records = cursor.fetchall()
        print(records)
        print("fetchall success!")
    except Error as e:
        print("Error reading data from MySQL tables", e)
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()
            print("MySQL connection is closed")
            return records