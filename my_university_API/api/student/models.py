# This file contain all models of student (this file is for Roberto)

####################################################################
#                             import
####################################################################
from api.student import student  # to use api
from flask_restx import fields  # to use Resource, that expose http request method

####################################################################
#                             model
####################################################################
contact_person = student.model('contact_person', {
    'tipo_contatto': fields.String,
    'valore_contatto': fields.String
})

student_model = student.model('student_model', {
    'cf': fields.String,
    'nome': fields.String,
    'cognome': fields.String,
    'data_di_nascita': fields.String,
    'luogo_di_nascita': fields.String,
    'cap': fields.String,
    'via_piazza': fields.String,
    'civico': fields.String,
    'matricola_studente': fields.String,
    'email_studente': fields.String,
    'data_immatricolazione': fields.String,
    'contatti': fields.List(fields.Nested(contact_person))})

login_student_model = student.model('login_student', {
    'matricola_studente': fields.String,
    'password_studente': fields.String
})
