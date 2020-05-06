# myUniversity
University project for the examination of web technologies, Parthenope 🎓

## API 
![Immagine di path](https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcROSC6b0CtrgxHuiMRgl1VynmK98NiRGdQjtyv5aE-mYpWYP0B_&usqp=CAU)

Le API sono organizzate in quattro namespace:
- API Segreteria (secretary '/segreteria' )
- API Docente (professor '/docente')
- API Stuedente (student '/studente')
- API Global (universal '/universal')

Inoltre gode di un prefisso, il quale utilizza questo path:

![Immagine di path](https://github.com/robertove93/myUniversity/blob/Developer/images/path_myUniversity.png?raw=true)

Vediamo ora nel dettaglio le nostre API:

#### API_Segreteria

![test](https://raw.githubusercontent.com/robertove93/myUniversity/Developer/images/Schermata%202020-05-04%20alle%2020.12.26.png)

Prevede la possibilità, da parte della segreteria, di poter inserire una sede.
```
Inserimento_sede(
  nome_Sede: string, 
  orario_apertura: int, 
  orario_chiusura: int,  
  numero_piani: int,   
  cap: int,
  via_piazza: string,
  civico: string)
  {
  inserimento in SEDE con 
  nome_Sede: string,
  orario_apertura: int,
  orario_chiusura: int, 
  numero_piani: int,
  cap: int,
  via_piazza: string,
  civico: string
  }
```

- GET
reperimento_sedi() --> utilizza dictionary [schema tabella Sede join con Indirizzo_Sede]
- DELETE
cancella_sede(nome_sede: string)

- POST
inserimento_aula(
  nome_sede: string,
  numero_piano: int,
  numero_aula: int,
  capienza: int)
- DELETE
cancella_aula(
 nome_sede: string
 numero_piano: int
 numero_aula: int)

- POST
inserimento_corso_laurea(
  codice_corso: string,
  nome_corso: string,
  durata_corso_laurea: int)
- GET
reperimento_corsi_laurea() --> utilizza dictionary [schema tabella corso_di_laurea]
- DELETE
cancella_corso_laurea(
codice_corso: string)

- POST
inserimento_ospitazione(
nome_sede: string,
codice_corso: string)
- GET
reperimento_ospitazioni() --> utilizza dictionary [JOIN tra Ospitazione e Corso_di_laurea]
- DELETE
cancella_ospitazione(
nome_sede: string
codice_corso: string)

- POST
inserimento_disciplina(
 codice_corso: string
 codice_disciplina: string
 nome_disciplina: string
 cfu: int
 semestre:int
 anno: int)
- GET
reperimento_discipline()--> utilizza dictionary [JOIN tra Disciplina e Corso_di_laurea(solo nome_corso_laurea)]
- DELETE
cancella_disciplina(
codice_corso: string
codice_disciplina: string
)
- POST ??
inserimento_docente(
  cf: string
  nome: string
  cognome: string
  data_di_nascita: date
  luogo_di_nascita: string
  matricola_docente: string
  email_docente: string
  password_docente: string
  cap: int
  via_piazza : string
  civico: string
)
{prevede:
insert in PERSONA
cf: string
nome: string
cognome: string
data_di_nascita: date
luogo_di_nascita: string
cap: int
via_piazza : string
civico: string)
insert in DOCENTE
 inserimento_docente(
 matricola_docente: string
 cf: string (uguale a quello di persona)
 mail_docente: string
 password_docente: string)

}

- GET
reperimento_docenti()--> utilizza dictionary [JOIN tra DOCENTE e PERSONA(senza valore password_docente) + select join tra PERSONA, CONTATTO_PERSONA e CONTATTO (per reperire a tutti i contatti di quella persona )]
- DELETE  ?? (eliminare prima docente e poi persona )
cancella_docente(
cf: string
matricola_docente: string)

- POST
assunzione_docenti(
matricola_docente: string,
codice_corso: string)

- GET
reperimento_assunzioni() --> utilizza dictionary[JOIN tra PERSONA, DOCENTE, LAVORA, CORSO_DI_LAUREA, OSPITAZIONE e SEDE]

- POST ??
inserimento_studente(
  cf: string
  nome: string
  cognome: string
  data_di_nascita: date
  luogo_di_nascita: string
  matricola_studente: string
  email_studente: string
  password_studente: string
  data_immatricolazione: date
  cap: int
  via_piazza : string
  civico: string)
{prevede:
insert in PERSONA
cf: string
nome: string
cognome: string
data_di_nascita: date
luogo_di_nascita: string
cap: int
via_piazza : string
civico: string)
insert in STUDENTE
 inserimento_studente(
 matricola_studente: string
 cf: string (uguale a quello di persona)
 mail_studente: string
 password_studente: string
 data_immatricolazione: date)

}

- GET
reperimento_studenti()--> utilizza dictionary [JOIN tra STUDENTE e PERSONA(senza valore password_studente) + select join tra PERSONA, CONTATTO_PERSONA e CONTATTO (per reperire a tutti i contatti di quella persona )]
- DELETE  ?? (eliminare prima studente e poi persona )
cancella_studente(
cf: string
matricola_studente: string)

- POST
inserimento_insegna(
matricola_docente: string
codice_corso: string
codice_disciplina: string)

- GET
reperimento_insegnamenti()--> utilizza dictionary [JOIN tra DISCIPLINA, INSEGNA, DOCENTE e PERSONA]

- DELETE
cancella_insegna(
matricola_docente: string
codice_corso: string
codice_disciplina: string
)

- POST
inserimento_lezione(
codice_corso: string
codice_disciplina: string
nome_sede: string
numero_piano: int
numero_aula: int
numero_lezione: int
data_inizio: dateTime
numero_ore: int
titolo: string
descrizione: string)

- DELETE
cancella_lezione(
codice_corso: string
codice_disciplina: string
nome_sede: string
numero_piano: int
numero_aula: int
numero_lezione: int)

- POST
insegnamento_docente(matricola_docente: string, codice_corso: string, codice_disciplina: string){
INSERT in INSEGNA
}
- GET 
reperimento_insegnamenti_docenti(){
JOIN tra PERSONA, DOCENTE, INSEGNA, DISCIPLINA, CORSO_DI_LAUREA, OSPITAZIONE, SEDE
}

#### API Docente
#### API Studente
- [ ] Progettare API studente
#### API Globali
- [ ] Progettare API Globali

## Dependencies

```
aniso8601==8.0.0
attrs==19.3.0
click==7.1.2
dnspython==1.16.0
Flask==1.1.2
flask-restx==0.2.0
importlib-metadata==1.6.0
itsdangerous==1.1.0
Jinja2==2.11.2
jsonschema==3.2.0
MarkupSafe==1.1.1
mysql-connector-python==8.0.19
protobuf==3.6.1
pyrsistent==0.16.0
python-dotenv==0.13.0
pytz==2020.1
six==1.14.0
Werkzeug==1.0.1
zipp==3.1.0
```
