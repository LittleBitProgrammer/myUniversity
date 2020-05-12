from api.student import *
from flask_restx import fields

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
    'matricola_studente': fields.String,
    'data_iscrizione': fields.String
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
    'nome': fields.String,
    'cognome': fields.String,
    'email_docente': fields.String,
    'motivazione_ricevimento': fields.String,
    'data_ricevimento': fields.String,
    'durata': fields.String
})


