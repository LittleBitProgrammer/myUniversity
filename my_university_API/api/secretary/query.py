# This file contain all query of the database

####################################################################
#                             DB_functions
####################################################################

# ========================== query to insert head office (insertHeadOffice) ==========================
mySQL_query_insert_head_office = """INSERT INTO sede(nome_sede,
                                                     orario_apertura,
                                                     orario_chiusura,
                                                     numero_piani,
                                                     cap,
                                                     via_piazza,
                                                     civico)
                                    VALUES(%s, %s, %s, %s, %s, %s, %s)"""

# ========================== query to get all head offices (get_all_offices) ==========================
mySQL_query_get_all_head_offices = """SELECT nome_sede,
                                             orario_apertura,
                                             orario_chiusura, 
                                             numero_piani,
                                             cap, 
                                             via_piazza, 
                                             civico
                                      FROM sede"""

mySQL_query_get_all_head_office_contacts = """SELECT tipo_contatto, valore_contatto 
                                              FROM contatto_sede
                                              WHERE nome_sede = %s"""

# ========================== query to insert head office ==========================

mySQL_query_insert_contact = """INSERT INTO contatto(tipo_contatto,valore_contatto)
                                VALUES(%s,%s)"""

mySQL_query_insert_head_office_contact = """INSERT INTO contatto_sede(nome_sede, tipo_contatto, valore_contatto)
                                            VALUES(%s,%s,%s)"""

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

mySQL_query_insert_room = """INSERT INTO aula(nome_sede, 
                                              numero_piano, 
                                              numero_aula, 
                                              capienza)
                             VALUES (%s, %s, %s, %s)"""

mySQL_query_delete_room_lesson = """DELETE FROM lezione
                                    WHERE nome_sede = %s
                                    AND numero_piano = %s 
                                    AND numero_aula = %s"""

mySQL_query_delete_room = """DELETE FROM aula
                             WHERE nome_sede = %s
                             AND numero_piano = %s
                             AND numero_aula = %s"""

mySQL_query_insert_degree_course = """INSERT INTO corso_di_laurea (codice_corso, nome_corso, durata_corso_laurea) 
                                      VALUES (%s, %s, %s)"""

mySQL_query_get_all_degree_courses = """SELECT codice_corso,
                                               nome_corso,
                                               durata_corso_laurea
                                        FROM corso_di_laurea"""

mySQL_query_delete_degree_course_location = """DELETE FROM ospitazione
                                 WHERE codice_corso = %s"""

mySQL_query_delete_is_in = """DELETE FROM appartiene
                              WHERE codice_corso = %s"""

mySQL_query_delete_work = """DELETE FROM lavora
                             WHERE codice_corso = %s"""

mySQL_query_delete_lesson = """DELETE FROM lezione
                               WHERE codice_corso = %s"""

mySQL_query_delete_degree_course_discipline = """DELETE FROM disciplina
                                   WHERE codice_corso = %s"""

mySQL_query_delete_alert = """DELETE FROM avviso
                              WHERE codice_corso = %s"""

mySQL_query_delete_teaching = """DELETE FROM insegna
                                 WHERE codice_corso = %s"""

mySQL_query_delete_followed_discipline = """DELETE FROM disciplina_seguita
                                            WHERE codice_corso = %s"""

mySQL_query_delete_newletter_subscription = """DELETE FROM iscrizione_newsletter
                                               WHERE codice_corso = %s"""

mySQL_query_delete_degree_course = """DELETE FROM corso_di_laurea
                                      WHERE codice_corso = %s"""

mySQL_query_insert_location = """INSERT INTO ospitazione (nome_sede, codice_corso) 
                                 VALUES (%s, %s)"""

mySQL_query_get_all_locations = """SELECT  corso_di_laurea.codice_corso, 
                                           corso_di_laurea.nome_corso, 
                                           corso_di_laurea.durata_corso_laurea,
                                           sede.nome_sede, 
                                           sede.orario_apertura,
                                           sede.orario_chiusura,
                                           sede.numero_piani,
                                           sede.cap,
                                           sede.via_piazza,
                                           sede.civico
                                   FROM corso_di_laurea 
                                   NATURAL JOIN ospitazione
                                   NATURAL JOIN sede"""

mySQL_query_delete_location = """DELETE FROM ospitazione
                                 WHERE nome_sede = %s
                                 AND codice_corso = %s"""

mySQL_query_insert_discipline = """INSERT INTO disciplina(codice_corso, 
                                                          codice_disciplina, 
                                                          nome_disciplina, 
                                                          cfu,
                                                          semestre,
                                                          anno)
                                   VALUES (%s, %s, %s, %s, %s, %s)"""

mySQL_query_get_all_discipline = """SELECT corso_di_laurea.nome_corso, 
                                           disciplina.nome_disciplina, 
                                           disciplina.codice_disciplina, 
                                           disciplina.cfu,disciplina.anno, 
                                           disciplina.semestre 
                                    FROM corso_di_laurea 
                                    NATURAL JOIN disciplina 
                                    ORDER BY corso_di_laurea.nome_corso"""

mySQL_query_delete_discipline_lesson = """DELETE FROM lezione
                                          WHERE codice_corso = %s
                                          AND codice_disciplina = %s"""

mySQL_query_delete_discipline_alert = """DELETE FROM avviso
                                         WHERE codice_corso = %s
                                         AND codice_disciplina = %s"""

mySQL_query_delete_discipline_teaching = """DELETE FROM insegna
                                            WHERE codice_corso = %s
                                            AND codice_disciplina = %s"""

mySQL_query_delete_discipline_followed_discipline = """DELETE FROM disciplina_seguita
                                                       WHERE codice_corso = %s
                                                       AND codice_disciplina = %s"""

mySQL_query_delete_discipline_newletter_subscription = """DELETE FROM iscrizione_newsletter
                                                          WHERE codice_corso = %s
                                                          AND codice_disciplina = %s"""

mySQL_query_delete_discipline = """DELETE FROM disciplina
                                   WHERE codice_corso = %s
                                   AND codice_disciplina = %s"""

mySql_insert_person = """INSERT INTO persona(cf, 
                                             nome,
                                             cognome, 
                                             data_di_nascita,
                                             luogo_di_nascita,
                                             cap,
                                             via_piazza,
                                             civico)  
                         VALUES (%s, %s, %s, %s, %s, %s, %s, %s) """

mySql_insert_teacher = """INSERT INTO docente(matricola_docente, 
                                              cf,
                                              email_docente,
                                              password_docente) 
                          VALUES (%s, %s, %s, %s) """

mySQL_query_get_all_teachers = """SELECT docente.matricola_docente, 
                                         persona.nome,
                                         persona.cognome,
                                         docente.email_docente,
                                         docente.cf,
                                         persona.data_di_nascita,
                                         persona.luogo_di_nascita,
                                         persona.cap,
                                         persona.via_piazza,
                                         persona.civico
                                  FROM docente
                                  NATURAL JOIN persona"""

mySQL_query_get_all_person_contacts = """SELECT tipo_contatto, valore_contatto 
                                         FROM contatto_persona 
                                         WHERE cf = %s"""

mySQL_query_delete_person_contacts = """DELETE FROM contatto_persona
                                         WHERE cf = %s"""

mySQL_query_delete_teacher_person = """DELETE FROM persona
                                       WHERE cf = %s"""

mySQL_query_delete_teacher_teach = """DELETE FROM insegna
                                      WHERE matricola_docente = %s"""

mySQL_query_delete_teacher_alert = """DELETE FROM avviso
                                      WHERE matricola_docente = %s"""

mySQL_query_delete_teacher_receipt = """DELETE FROM ricevimento
                                        WHERE matricola_docente = %s"""

mySQL_query_delete_teacher = """DELETE FROM docente
                                WHERE matricola_docente = %s"""

mySQL_query_delete_contact = """DELETE FROM contatto
                                WHERE tipo_contatto = %s
                                AND  valore_contatto = %s"""

mySQL_query_select_contact = """SELECT tipo_contatto, valore_contatto
                                FROM contatto_persona
                                WHERE cf = %s"""

mySQL_query_delete_teacher_receipt_request = """DELETE FROM richiesta_ricevimento
                                                WHERE matricola_docente = %s"""

mySql_insert_persona = """INSERT INTO persona(cf, 
                                              nome,
                                              cognome, 
                                              data_di_nascita,
                                              luogo_di_nascita,
                                              cap,
                                              via_piazza,
                                              civico)  
                           VALUES (%s, %s, %s, %s, %s, %s, %s, %s) """

mySql_insert_studente = """INSERT INTO studente(matricola_studente, 
                                                cf,
                                                email_studente,
                                                data_immatricolazione,
                                                password_studente) 
                           VALUES (%s, %s, %s, %s, %s) """

mySql_insert_is_in = """INSERT INTO appartiene(codice_corso, matricola_studente) 
                        VALUES (%s, %s)"""

mySQL_query_get_all_students = """SELECT studente.matricola_studente, 
                                         persona.nome,
                                         persona.cognome,
                                         studente.email_studente,
                                         studente.data_immatricolazione,
                                         studente.cf,
                                         persona.data_di_nascita,
                                         persona.luogo_di_nascita,
                                         persona.cap,
                                         persona.via_piazza,
                                         persona.civico
                                  FROM studente
                                  NATURAL JOIN persona"""

mySQL_query_get_all_contact = """SELECT tipo_contatto, valore_contatto 
                                 FROM contatto_persona 
                                 WHERE cf = %s"""

mySQL_query_delete_teach = """DELETE FROM insegna
                              WHERE matricola_docente = %s
                              AND codice_corso = %s
                              AND codice_disciplina = %s"""

mySQL_query_insert_teach = """INSERT INTO insegna(matricola_docente, codice_corso, codice_disciplina) 
                              VALUES (%s, %s, %s)"""
# ===================

mySQL_query_delete_student_person = """DELETE FROM persona
                                       WHERE cf = %s"""

mySQL_query_delete_student = """DELETE FROM studente
                                 WHERE matricola_studente = %s"""

mySQL_query_delete_student_receipt_request = """DELETE FROM richiesta_ricevimento
                                                WHERE matricola_studente = %s"""

mySQL_query_delete_student_newsletter = """DELETE FROM iscrizione_newsletter 
                                           WHERE matricola_studente = %s"""

mySQL_query_delete_student_followed_discipline = """DELETE FROM disciplina_seguita 
                                                    WHERE matricola_studente = %s"""

mySQL_query_delete_student_is_in = """DELETE FROM appartiene 
                                           WHERE matricola_studente = %s"""

mySQL_query_get_all_teachings = """SELECT docente.matricola_docente, 
                                          persona.nome, 
                                          persona.cognome, 
                                          docente.email_docente, 
                                          corso_di_laurea.nome_corso, 
                                          disciplina.codice_disciplina, 
                                          disciplina.nome_disciplina, 
                                          disciplina.cfu, 
                                          disciplina.anno, 
                                          disciplina.semestre, 
                                          sede.nome_sede,
                                          sede.via_piazza,
                                          sede.civico,
                                          sede.orario_apertura,
                                          sede.orario_chiusura
                                    FROM persona 
                                    INNER JOIN docente ON persona.cf = docente.cf
                                    INNER JOIN insegna ON docente.matricola_docente = insegna.matricola_docente
                                    INNER JOIN disciplina ON insegna.codice_corso = disciplina.codice_corso and insegna.codice_disciplina = disciplina.codice_disciplina
                                    INNER JOIN corso_di_laurea ON disciplina.codice_corso = corso_di_laurea.codice_corso
                                    INNER JOIN ospitazione ON corso_di_laurea.codice_corso = ospitazione.codice_corso
                                    INNER JOIN sede ON ospitazione.nome_sede = sede.nome_sede
                                    ORDER BY docente.matricola_docente"""