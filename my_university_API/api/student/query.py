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

mySQL_query_get_student_contacts = """SELECT tipo_contatto, valore_contatto
                                      FROM contatto_persona
                                      WHERE cf = %s"""

mySQL_query_update_password = """UPDATE studente 
                                 SET password_studente = %s 
                                 WHERE (matricola_studente = %s 
                                 AND password_studente = %s)"""

mySQL_query_follow_discipline = """INSERT INTO disciplina_seguita(codice_corso, codice_disciplina, matricola_studente)
                                   VALUES(%s, %s, %s)"""

mySQL_query_delete_follow_discipline = """DELETE FROM disciplina_seguita
                                          WHERE codice_corso = %s
                                          AND codice_disciplina = %s
                                          AND matricola_studente = %s"""

mySQL_query_get_calendar = """SELECT disciplina_seguita.codice_corso,
                                     corso_di_laurea.nome_corso,
                                     doc.matricola_docente,
                                     doc.nome,
                                     doc.cognome,
                                     disciplina_seguita.codice_disciplina,
                                     disciplina.nome_disciplina,
                                     lezione.nome_sede,
                                     lezione.numero_piano,
                                     lezione.numero_aula,
                                     lezione.numero_ore,
                                     lezione.data_inizio,
                                     lezione.titolo,
                                     lezione.descrizione
                               FROM studente
                               NATURAL JOIN disciplina_seguita
                               NATURAL JOIN disciplina
                               NATURAL JOIN corso_di_laurea
                               NATURAL JOIN lezione
                               NATURAL JOIN aula
                               NATURAL JOIN sede
                               INNER JOIN (SELECT *  FROM persona
                                           NATURAL JOIN docente
                                           NATURAL JOIN insegna) AS doc
                               ON disciplina.codice_disciplina = doc.codice_disciplina
                               WHERE studente.matricola_studente = %s"""