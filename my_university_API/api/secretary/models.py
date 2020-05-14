from api.secretary import secretary
from flask_restx import fields

####################################################################
#                             Convenzioni:
#   *nome_model*_model = secretary.model('*nome model* model',{
#       'chiave': fields.*tipo*
#        ...
#    })
####################################################################

nested_contact_model = secretary.model('nested contact teacher model', {
    'tipo_contatto': fields.String,
    'valore_contatto': fields.String
})

insert_student_model = secretary.model('insert student model', {
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
    'password_studente': fields.String,
    'codice_corso': fields.String
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

get_head_office_model = secretary.inherit('get_head_office_model', insert_headoffice_model, {
    'contatti': fields.List(fields.Nested(nested_contact_model))
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

delete_degree_course_model = secretary.model('delete degree course model', {
    'codice_corso': fields.String
})

insert_location_model = secretary.model('insert location module', {
    'nome_sede': fields.String,
    'codice_corso': fields.String
})

get_all_location_model = secretary.model('get all location model', {
    'codice_corso': fields.String,
    'nome_corso': fields.String,
    'durata_corso_laurea': fields.Integer,
    'nome_sede': fields.String,
    'orario_apertura': fields.Integer,
    'orario_chiusura': fields.Integer,
    'numero_piani': fields.Integer,
    'cap': fields.Integer,
    'via_piazza': fields.String,
    'civico': fields.String
})

insert_discipline_model = secretary.model('insert discipline', {
    'codice_corso': fields.String,
    'codice_disciplina': fields.String,
    'nome_disciplina': fields.String,
    'cfu': fields.Integer,
    'semestre': fields.Integer,
    'anno': fields.Integer
})

get_all_discipline_model = secretary.model('get all discipline model', {
    'nome_corso': fields.String,
    'nome_disciplina': fields.String,
    'codice_disciplina': fields.String,
    'cfu': fields.Integer,
    'anno': fields.Integer,
    'semestre': fields.Integer
})

delete_discipline_model = secretary.model('delete discipline module', {
    'codice_corso': fields.String,
    'codice_disciplina': fields.String
})

insert_teacher_model = secretary.model('insert teacher model', {
    'cf': fields.String,
    'nome': fields.String,
    'cognome': fields.String,
    'data_di_nascita': fields.String,
    'luogo_di_nascita': fields.String,
    'cap': fields.Integer,
    'via_piazza': fields.String,
    'civico': fields.String,
    'matricola_docente': fields.String,
    'email_docente': fields.String,
    'password_docente': fields.String
})

get_all_teacher_model = secretary.model('get all teacher model', {
    'matricola_docente': fields.String,
    'nome': fields.String,
    'cognome': fields.String,
    'email_docente': fields.String,
    'cf': fields.String,
    'data_di_nascita': fields.String,
    'luogo_di_nascita': fields.String,
    'cap': fields.Integer,
    'via_piazza': fields.String,
    'civico': fields.String,
    'contatti': fields.List(fields.Nested(nested_contact_model))
})

delete_teacher_model = secretary.model('delete teacher model', {
    'cf': fields.String,
    'matricola_docente': fields.String
})

get_all_student_model = secretary.model('get all student model', {
    'matricola_studente': fields.String,
    'nome': fields.String,
    'cognome': fields.String,
    'email_studente': fields.String,
    'data_immatricolazione': fields.String,
    'anno_in_corso': fields.Integer,
    'cf': fields.String,
    'data_di_nascita': fields.String,
    'luogo_di_nascita': fields.String,
    'cap': fields.Integer,
    'via_piazza': fields.String,
    'civico': fields.String,
    'contatti': fields.List(fields.Nested(nested_contact_model))
})

delete_teach_model = secretary.model('delete teach model', {
    'matricola_docente': fields.String,
    'codice_corso': fields.String,
    'codice_disciplina': fields.String
})

delete_student_model = secretary.model('delete student model', {
    'cf': fields.String,
    'matricola_studente': fields.String
})

get_all_teachings_model = secretary.model('get all teachings model', {
    'matricola_docente': fields.String,
    'nome': fields.String,
    'cognome': fields.String,
    'email_docente': fields.String,
    'nome_corso': fields.String,
    'codice_disciplina': fields.String,
    'nome_disciplina': fields.String,
    'cfu': fields.Integer,
    'anno': fields.Integer,
    'semestre': fields.Integer,
    'nome_sede': fields.String,
    'via_piazza': fields.String,
    'civico': fields.String,
    'orario_apertura': fields.Integer,
    'orario_chiusura': fields.Integer
})

update_anno_in_corso_studente_model = secretary.model('update anno in corso studente model', {
    'matricola_studente': fields.String,
    'anno_in_corso': fields.Integer
})
