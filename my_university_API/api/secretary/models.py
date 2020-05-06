from api.secretary import secretary
from flask_restx import fields

insert_student_model = secretary.model('insert student model', {
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
    'password_studente': fields.String
})

insert_headoffice_model = secretary.model('insert headoffice model', {
    'nome_sede': fields.String,
    'orario_apertura': fields.Integer,
    'orario_chiusura': fields.Integer,
    'numero_piani': fields.Integer,
    'cap': fields.Integer,
    'via_piazza': fields.String,
    'civico': fields.String
})
