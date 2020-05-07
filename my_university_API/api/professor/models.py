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

update_password_professor = professor.model('update_password_professor', {
    'nuova_password_docente': fields.String,
    'matricola_docente': fields.String,
    'password_docente': fields.String

})

freshman_professor = professor.model('freshman_professor', {
    'matricola_docente': fields.String
})

get_teachings_professor = professor.model('get_teachings_professor',{
    'matricola_docente': fields.String,
    'codice_corso': fields.String,
    'codice_disciplina': fields.String,
    'nome_disciplina': fields.String,
    'cfu': fields.String,
    'semestre': fields.String,
    'anno': fields.String,
    'nome_corso': fields.String,
    'durata_corso_laurea': fields.String,
    'nome_sede': fields.String,
    'orario_apertura': fields.String,
    'orario_chiusura': fields.String,
    'numero_piani': fields.String,
    'cap': fields.String,
    'via_piazza': fields.String,
    'civico': fields.String
})