# This file contain all models of student (this file is for Roberto)

####################################################################
#                             import
####################################################################
from application.api.student import student  # to use api
from flask_restx import fields  # to use Resource, that expose http request method

####################################################################
#                             model
####################################################################


freshman_student = student.model('freshman_student', {
    'matricola_studente': fields.String
})

insert_richiesta_ricevimento_model = student.model('insert_richiesta_ricevimento_model',{
    'matricola_docente': fields.String,
    'data_ricevimento': fields.String,
    'matricola_studente': fields.String,
    'motivazione_ricevimento': fields.String
})

delete_richiesta_ricevimento_model = student.model('delete_richiesta_ricevimento_model',{
    'matricola_docente': fields.String,
    'data_ricevimento': fields.String,
    'matricola_studente': fields.String
})


insert_iscrizione_newsletter_model = student.model('insert_iscrizione_newsletter_model',{
    'codice_corso': fields.String,
    'codice_disciplina': fields.String,
    'matricola_studente': fields.String
})

get_news_student_model = student.model('get_news_student_model',{
    'nome': fields.String,
    'cognome': fields.String,
    'email_docente': fields.String,
    'codice_disciplina': fields.String,
    'nome_disciplina': fields.String,
    'data_avviso': fields.String,
    'titolo_avviso': fields.String,
    'corpo_avviso': fields.String
})

get_prenotazioni_ricevimento_model = student.model('get_prenotazioni_ricevimento_model',{
    'data_ricevimento': fields.String,
    'matricola_docente': fields.String,
    'nome': fields.String,
    'cognome': fields.String,
    'email_docente': fields.String,
    'motivazione_ricevimento': fields.String,
    'data_ricevimento': fields.String,
    'ora_inizio': fields.String,
    'durata': fields.String
})

contact_person_model = student.model('contact person model', {
    'tipo_contatto': fields.String,
    'valore_contatto': fields.String
})

student_model = student.model('student model', {
    'cf': fields.String,
    'nome': fields.String,
    'cognome': fields.String,
    'data_di_nascita': fields.String,
    'luogo_di_nascita': fields.String,
    'cap': fields.Integer,
    'via_piazza': fields.String,
    'civico': fields.String,
    'matricola_studente': fields.String,
    'email_studente': fields.String,
    'data_immatricolazione': fields.String,
    'anno_in_corso': fields.Integer,
    'contatti': fields.List(fields.Nested(contact_person_model))})

login_student_model = student.model('login student model', {
    'matricola_studente': fields.String,
    'password_studente': fields.String
})

update_password_student_model = student.model('update password student model', {
    'nuova_password_studente': fields.String,
    'matricola_studente': fields.String,
    'password_studente': fields.String
})

follow_discipline_model = student.model('follow discipline module', {
    'codice_corso': fields.String,
    'codice_disciplina': fields.String,
    'matricola_studente': fields.String
})

get_calendar_student_model = student.model('get_calendar_student_model', {
    'matricola_studente': fields.String
})

calendar_model = student.model('calendar model', {
    'codice_corso': fields.String,
    'nome_corso': fields.String,
    'matricola_docente': fields.String,
    'nome': fields.String,
    'cognome': fields.String,
    'codice_disciplina': fields.String,
    'nome_disciplina': fields.String,
    'nome_sede': fields.String,
    'numero_piano': fields.Integer,
    'numero_aula': fields.Integer,
    'numero_ore': fields.Integer,
    'data_inizio': fields.String,
    'titolo': fields.String,
    'descrizione': fields.String
})

lista_docenti_iscritti_corso_piu_newsletter_per_chat_model = student.model('lista_docenti_iscritti_corso_piu_newsletter_per_chat_model', {
    'cf': fields.String,
    'nome': fields.String,
    'cognome': fields.String,
    'matricola_docente': fields.String,
    'email_docente': fields.String,
    'codice_disciplina': fields.String,
    'nome_disciplina': fields.String,
    'contatti': fields.List(fields.Nested(contact_person_model))
})


lista_ricevimenti_prenotabili_model = student.model('get_lista_possibili_ricevimenti_model', {
    'data_ricevimento': fields.String,
    'ore_ricevimento': fields.String,
    'matricola_docente': fields.String,
    'email_docente': fields.String,
    'nome': fields.String,
    'cognome': fields.String
})

lista_discipline_model = student.model('lista_discipline_model', {
    'codice_corso': fields.String,
    'nome_corso': fields.String,
    'codice_disciplina': fields.String,
    'nome_disciplina': fields.String,
    'anno': fields.String,
    'semestre': fields.String,
    'cfu': fields.String
})

lista_discipline_seguite_model = student.model('lista_discipline_seguite_model', {
    'codice_corso': fields.String,
    'codice_disciplina': fields.String
})

lista_iscrizioni_newsletter_model = student.model('lista_discipline_seguite_model', {
    'codice_corso': fields.String,
    'codice_disciplina': fields.String,
    'data_iscrizione': fields.String
})