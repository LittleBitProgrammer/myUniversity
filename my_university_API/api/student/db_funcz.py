from mysql.connector import Error

def insert_richiesta_ricevimento(matricola_docente,
                                 data_ricevimento,
                                 matricola_studente,
                                 motivazione_ricevimento,
                                 connection):
    try:
        cursor = connection.cursor()
        sql_insert_richiesta_ricevimento_Query = """ 
        INSERT INTO richiesta_ricevimento 
        (matricola_docente, data_ricevimento, matricola_studente, motivazione_ricevimento) 
        VALUES (%s, %s, %s, %s);"""

        print('matricola_docente', matricola_docente)
        print('data_ricevimento', data_ricevimento)
        print('matricola_studente', matricola_studente)
        print('motivazione_ricevimento', motivazione_ricevimento)

        insert_tuple = (matricola_docente, data_ricevimento, matricola_studente, motivazione_ricevimento)
        cursor = connection.cursor(dictionary=True)
        cursor.execute(sql_insert_richiesta_ricevimento_Query, insert_tuple)
        connection.commit()
        print("Richiesta ricevimento inviata!")
    except Error as e:
        print("Error from MySQL", e)
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()
            print("MySQL connection is closed")

def delete_richiesta_ricevimento(matricola_docente,
                                 data_ricevimento,
                                 matricola_studente,
                                 connection):
    try:
        cursor = connection.cursor()
        sql_delete_richiesta_ricevimento_Query = """ 
            DELETE FROM richiesta_ricevimento
            WHERE matricola_docente  = %s
            AND data_ricevimento = %s
            AND matricola_studente = %s """

        print('matricola_docente', matricola_docente)
        print('data_ricevimento', data_ricevimento)
        print('matricola_studente', matricola_studente)

        delete_tuple = (matricola_docente, data_ricevimento, matricola_studente)
        cursor = connection.cursor(dictionary=True)
        cursor.execute(sql_delete_richiesta_ricevimento_Query, delete_tuple)
        connection.commit()
        print("delete Richiesta ricevimento effettuata!")
    except Error as e:
        print("Error from MySQL", e)
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()
            print("MySQL connection is closed")

def insert_iscrizione_newsletter(codice_corso,
                                 codice_disciplina,
                                 matricola_studente,
                                 data_iscrizione,
                                 connection):
    try:
        cursor = connection.cursor()
        sql_insert_richiesta_ricevimento_Query = """ 
        INSERT INTO iscrizione_newsletter 
        (codice_corso, codice_disciplina, matricola_studente, data_iscrizione) 
        VALUES (%s, %s, %s, %s);"""

        print('codice_corso', codice_corso)
        print('codice_disciplina', codice_disciplina)
        print('matricola_studente', matricola_studente)
        print('data_iscrizione', data_iscrizione)

        insert_tuple = (codice_corso, codice_disciplina, matricola_studente, data_iscrizione)
        cursor = connection.cursor(dictionary=True)
        cursor.execute(sql_insert_richiesta_ricevimento_Query, insert_tuple)
        connection.commit()
        print("Iscrizione newsletter effettuata!")
    except Error as e:
        print("Error from MySQL", e)
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()
            print("MySQL connection is closed")

def reperimento_news_studente(matricola_studente, connection):
    records = []
    try:
        cursor = connection.cursor()
        sql_select_Query = """    SELECT persona.nome, persona.cognome, docente.email_docente, 
                                    avviso.codice_disciplina, disciplina.nome_disciplina, 
                                    avviso.data_avviso, avviso.titolo_avviso, avviso.corpo_avviso
                                    FROM iscrizione_newsletter
                                    INNER JOIN disciplina
                                    ON( iscrizione_newsletter.codice_corso = disciplina.codice_corso 
                                        AND iscrizione_newsletter.codice_disciplina = disciplina.codice_disciplina)
                                    INNER JOIN avviso
                                    ON(disciplina.codice_corso = avviso.codice_corso 
                                        AND disciplina.codice_disciplina = avviso.codice_disciplina)
                                    INNER JOIN docente
                                    ON avviso.matricola_docente = docente.matricola_docente
                                    INNER JOIN persona
                                    ON docente.cf = persona.cf
                                    WHERE iscrizione_newsletter.matricola_studente = %s
                                    ORDER BY avviso.data_avviso DESC;"""
        student_tuple = (matricola_studente,)
        cursor = connection.cursor(dictionary=True)
        cursor.execute(sql_select_Query, student_tuple)
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

def reperimento_prenotazioni_ricevimento_studente(matricola_studente, connection):
    records = []
    try:
        cursor = connection.cursor()
        sql_select_Query = """SELECT
            richiesta_ricevimento.data_ricevimento,
            persona.nome, persona.cognome,
            docente.email_docente,
            richiesta_ricevimento.motivazione_ricevimento,
            richiesta_ricevimento.data_ricevimento,
            richiesta_ricevimento.durata
            FROM richiesta_ricevimento
            inner join ricevimento
            on richiesta_ricevimento.matricola_docente = richiesta_ricevimento.matricola_docente 
                and richiesta_ricevimento.data_ricevimento = ricevimento.data_ricevimento
            inner join docente
            on richiesta_ricevimento.matricola_docente = docente.matricola_docente
            inner join persona
            on docente.cf = persona.cf
            where richiesta_ricevimento.matricola_studente = %s
            ORDER by richiesta_ricevimento.data_ricevimento DESC;"""
        student_tuple = (matricola_studente,)
        cursor = connection.cursor(dictionary=True)
        cursor.execute(sql_select_Query, student_tuple)
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

