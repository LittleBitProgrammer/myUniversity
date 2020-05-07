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

insert_headoffice_model = secretary.model('insert head office model', {
    'nome_sede': fields.String,
    'orario_apertura': fields.Integer,
    'orario_chiusura': fields.Integer,
    'numero_piani': fields.Integer,
    'cap': fields.Integer,
    'via_piazza': fields.String,
    'civico': fields.String
})

nested_contact_head_office_model = secretary.model('nested contact head office model', {
    'nome_sede': fields.String,
    'tipo_contatto': fields.String,
    'valore_contatto': fields.String
})

get_head_office_model = secretary.inherit('get_head_office_model', insert_headoffice_model,{
    'contatti': fields.List(fields.Nested(nested_contact_head_office_model))
})

insert_contact_model = secretary.model('insert contact model', {
    'nome_sede': fields.String,
    'tipo_contatto': fields.String,
    'valore_contatto': fields.String
})

delete_head_office_model = secretary.model('delete head office model', {
    'nome_sede': fields.String
})

insert_room_model = secretary.model('insert room model', {
    'nome_sede': fields.String,
    'numero_piano': fields.Integer,
    'numero_aula': fields.Integer,
    'capienza': fields.Integer
})

delete_room_model = secretary.model('delete room model', {
    'nome_sede': fields.String,
    'numero_piano': fields.Integer,
    'numero_aula': fields.Integer
})

insert_degree_course_model = secretary.model('insert degree course model', {
    'codice_corso': fields.String,
    'nome_corso': fields.String,
    'durata_corso_laurea': fields.Integer
})


