from api.professor import *
from flask_restx import fields

contact_person = professor.model('contact_person', {
    'tipo_contatto': fields.String,
    'valore_contatto': fields.String
})

professor_model = professor.model('professor_model', {
    'cf': fields.String,
    'nome': fields.String,
    'cognome': fields.String,
    'data_di_nascita': fields.String,
    'luogo_di_nascita': fields.String,
    'cap': fields.String,
    'via_piazza': fields.String,
    'civico': fields.String,
    'matricola_docente': fields.String,
    'email_docente': fields.String,
    'contatti': fields.List(fields.Nested(contact_person))})

login_professor = professor.model('login_professor', {
    'matricola_docente': fields.String,
    'password_docente': fields.String
})