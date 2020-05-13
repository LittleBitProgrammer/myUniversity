# This file contain all models of student (this file is for Roberto)

####################################################################
#                             import
####################################################################
from api.student import student  # to use api
from flask_restx import fields  # to use Resource, that expose http request method

####################################################################
#                             model
####################################################################
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
