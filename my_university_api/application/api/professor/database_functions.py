# This file contain all database functions of the secretary

####################################################################
#                             import
####################################################################
from mysql.connector import Error  # to use error
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

####################################################################
#                             DB_functions
####################################################################
def loginProfessor(matricola_docente, password_docente, connection):
    records = []

    try:
        cursor = connection.cursor()
        sql_select_Query_login = """
        SELECT password_docente from docente where  matricola_docente = %s;
        """
        professor_chk_psw = (matricola_docente,)
        cursor = connection.cursor(dictionary=True)
        cursor.execute(sql_select_Query_login, professor_chk_psw)
        psw = cursor.fetchall()

        print(psw[0]['password_docente'])
        try:
            authenticate = bcrypt.check_password_hash(psw[0]['password_docente'], password_docente)
        except:
            print("error")
        finally:
            print(authenticate)

        authenticate = bcrypt.check_password_hash(psw[0]['password_docente'], password_docente)
        if authenticate:
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
                                            WHERE docente.matricola_docente = %s"""
            professor_tuple = (matricola_docente, )
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
        else:
            records = []
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
        sql_select_Query_login = """
                SELECT password_docente from docente where  matricola_docente = %s;
                """
        professor_chk_psw = (matricola_docente,)
        cursor = connection.cursor(dictionary=True)
        cursor.execute(sql_select_Query_login, professor_chk_psw)
        psw = cursor.fetchall()

        pw_hash = bcrypt.generate_password_hash(nuova_password_docente)
        try:
            authenticate = bcrypt.check_password_hash(psw[0]['password_docente'], password_docente)
        except:
            print("error")
        finally:
            print(authenticate)

        authenticate = bcrypt.check_password_hash(psw[0]['password_docente'], password_docente)

        if authenticate:
            sql_update_password_Query = """ UPDATE docente 
                                            SET password_docente = %s 
                                            WHERE matricola_docente = %s ;"""

            professor_tuple = (pw_hash, matricola_docente)
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

def inserimento_ricevimento(matricola_docente,
                               data_ricevimento,
                               ore_ricevimento,
                               connection):
    try:
        cursor = connection.cursor()
        sql_insert_new_Query = """INSERT INTO ricevimento 
                                    (matricola_docente,
                                    data_ricevimento, 
                                    ore_ricevimento) 
                                    VALUES (%s, %s, %s);"""
        new_tuple = (matricola_docente, data_ricevimento, ore_ricevimento)
        cursor = connection.cursor(dictionary=True)
        cursor.execute(sql_insert_new_Query, new_tuple)
        connection.commit()
        print("Record inserted successfully into Ricevimento table")
    except Error as error:
        print(f"Failed to insert into MySQL table {error}")
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def delete_ricevimento(matricola_docente,
                        data_ricevimento,
                        connection):
    try:
        new_tuple = (matricola_docente, data_ricevimento)
        cursor = connection.cursor()
        sql_delete_richiesta_ricevimento_Query = """DELETE FROM richiesta_ricevimento 
                                  WHERE matricola_docente = %s AND data_ricevimento = %s;"""
        cursor = connection.cursor(dictionary=True)
        cursor.execute(sql_delete_richiesta_ricevimento_Query, new_tuple)
        sql_delete_ricevimento_Query = """DELETE FROM ricevimento 
                                  WHERE matricola_docente = %s AND data_ricevimento = %s;"""
        new_tuple = (matricola_docente, data_ricevimento)
        cursor = connection.cursor(dictionary=True)
        cursor.execute(sql_delete_ricevimento_Query, new_tuple)
        connection.commit()
        print("Record deleted successfully from Ricevimento table")
    except Error as error:
        print(f"Failed to delete from MySQL table {error}")
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def reperimento_info_ricevimenti(matricola_docente, connection):
    records = []
    try:
        cursor = connection.cursor()
        sql_select_ricevimento = """SELECT data_ricevimento,
                                           ore_ricevimento
                                    FROM ricevimento
                                    WHERE matricola_docente = %s"""
        print("matricola_docente : ", matricola_docente)
        professor_tuple = (matricola_docente,)
        cursor = connection.cursor(dictionary=True)
        cursor.execute(sql_select_ricevimento, professor_tuple)
        records = cursor.fetchall()

        print(records)
        sql_query_richiesta_ricevimento_info = """
                                             SELECT 
                                             richiesta_ricevimento.matricola_studente, 
                                             persona.nome, persona.cognome, studente.email_studente,
                                             richiesta_ricevimento.motivazione_ricevimento,
                                             richiesta_ricevimento.ora_inizio,
                                             richiesta_ricevimento.durata
                                             FROM richiesta_ricevimento
                                             INNER JOIN studente ON richiesta_ricevimento.matricola_studente = studente.matricola_studente
                                             INNER JOIN persona ON studente.cf = persona.cf
                                             WHERE richiesta_ricevimento.matricola_docente = %s AND richiesta_ricevimento.data_ricevimento = %s"""

        i = 0
        while i < len(records):
            record_tuple_info = (matricola_docente, records[i]['data_ricevimento'])
            cursor.execute(sql_query_richiesta_ricevimento_info, record_tuple_info)
            richiesta_records = cursor.fetchall()
            records[i]['prenotazioni'] = richiesta_records

            i += 1

        i = 0
        while i < len(records):
            sql_select_contatti_studente = """SELECT tipo_contatto,
                                                valore_contatto
                                                FROM contatto_persona
                                                WHERE cf = (SELECT cf FROM persona NATURAL JOIN studente WHERE matricola_studente = %s)"""

            j = 0
            print("num_prenotazioni x ricevimento", len(records[i]["prenotazioni"]))
            while j < len(records[i]["prenotazioni"]):


                record_tuple_info_mat_stud = (records[i]["prenotazioni"][j]["matricola_studente"],)
                cursor.execute(sql_select_contatti_studente, record_tuple_info_mat_stud)
                contatti_stud = cursor.fetchall()
                print(contatti_stud)
                records[i]["prenotazioni"][j]["contatti"] = contatti_stud
                j += 1

            i += 1


        print("Fetching each row using column name")
    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()
            print("MySQL connection is closed")
            return records

def update_richiesta_ricevimento(matricola_docente,
                                 data_ricevimento,
                                 matricola_studente,
                                 ora_inizio,
                                 durata,
                                 connection):
    try:
        cursor = connection.cursor()
        sql_update_richiesta_ricevimento_Query = """ UPDATE richiesta_ricevimento 
                                        SET 
                                        ora_inizio = %s ,
                                        durata = %s 
                                        WHERE matricola_docente = %s AND data_ricevimento = %s AND matricola_studente = %s """

        print('ora_inizio', ora_inizio)
        print('durata', durata)
        print('matricola_docente', matricola_docente)
        print('data_ricevimento', data_ricevimento)
        print('matricola_studente', matricola_studente)

        update_tuple = (ora_inizio, durata, matricola_docente, data_ricevimento, matricola_studente)
        cursor = connection.cursor(dictionary=True)
        cursor.execute(sql_update_richiesta_ricevimento_Query, update_tuple)
        connection.commit()
        print("Updated!")
    except Error as e:
        print("Error from MySQL", e)
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()
            print("MySQL connection is closed")



def reperimentoInfoStudentiCorsiENewsletter(matricola_docente, connection):
    students = []

    try:
        cursor = connection.cursor(dictionary=True)
        professor_tuple = (matricola_docente, matricola_docente)
        lista_studenti_iscritti_corso_piu_newsletter_per_chat = """
            SELECT persona.cf, persona.nome, persona.cognome, studente.matricola_studente, 
            studente.email_studente, studente.anno_in_corso, corso_di_laurea.codice_corso, 
            corso_di_laurea.nome_corso, disciplina.codice_disciplina, disciplina.nome_disciplina
            FROM persona 
            INNER JOIN studente on persona.cf = studente.cf
            INNER JOIN disciplina_seguita on studente.matricola_studente = disciplina_seguita.matricola_studente
            INNER JOIN disciplina on disciplina_seguita.codice_corso = disciplina.codice_corso and disciplina_seguita.codice_disciplina = disciplina.codice_disciplina
            INNER JOIN corso_di_laurea on disciplina.codice_corso = corso_di_laurea.codice_corso
            INNER JOIN insegna on disciplina.codice_corso = insegna.codice_corso and disciplina.codice_disciplina = insegna.codice_disciplina
            WHERE insegna.matricola_docente = %s
            UNION
            SELECT persona.cf, persona.nome, persona.cognome, studente.matricola_studente, 
            studente.email_studente, studente.anno_in_corso, corso_di_laurea.codice_corso, 
            corso_di_laurea.nome_corso, disciplina.codice_disciplina, disciplina.nome_disciplina
            FROM persona 
            INNER JOIN studente on persona.cf = studente.cf
            INNER JOIN iscrizione_newsletter on studente.matricola_studente = iscrizione_newsletter.matricola_studente
            INNER JOIN disciplina on iscrizione_newsletter.codice_corso = disciplina.codice_corso and iscrizione_newsletter.codice_disciplina = disciplina.codice_disciplina
            INNER JOIN corso_di_laurea on disciplina.codice_corso = corso_di_laurea.codice_corso
            INNER JOIN insegna on disciplina.codice_corso = insegna.codice_corso and disciplina.codice_disciplina = insegna.codice_disciplina
            WHERE insegna.matricola_docente = %s 
            """
        cursor.execute(lista_studenti_iscritti_corso_piu_newsletter_per_chat, professor_tuple)
        students = cursor.fetchall()

        mySQL_query_get_student_contacts = """SELECT tipo_contatto, valore_contatto
                                              FROM contatto_persona
                                              WHERE cf = %s"""

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