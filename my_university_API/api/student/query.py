# This file contain all student query of the database

####################################################################
#                                Query
####################################################################

mySQL_query_login_studente = """SELECT persona.cf,
                                       persona.nome,
                                       persona.cognome, 
                                       persona.data_di_nascita, 
                                       persona.luogo_di_nascita, 
                                       persona.cap, 
                                       persona.via_piazza, 
                                       persona.civico, 
                                       studente.matricola_studente,
                                       studente.email_studente, 
                                       studente.data_immatricolazione
                                FROM persona INNER JOIN studente 
                                ON persona.cf = studente.cf 
                                WHERE studente.matricola_studente = %s
                                AND studente.password_studente = %s"""

mysql_query_get_student_contacts = """SELECT tipo_contatto, valore_contatto
                                      FROM contatto_persona
                                      WHERE cf = %s"""

mysql_query_update_password = """UPDATE studente 
                                 SET password_studente = %s 
                                 WHERE (matricola_studente = %s 
                                 AND password_studente = %s)"""

mysql_query_follow_discipline = """INSERT INTO disciplina_seguita(codice_corso, codice_disciplina, matricola_studente)
                                   VALUES(%s, %s, %s)"""