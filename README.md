# myUniversity
University project for the examination of web technologies, Parthenope 🎓

## [API] (http://my-university-api.herokuapp.com/api/)
* Secretary
* Professor
* Student
* Mongodb

## Secretary

### POST /secretary/aggiorna_anno_in_corso

parametri | descrizione
------------ | -------------
matricola_studente|matricola studente
anno_in_corso |anno in corso

#### Response

Cambia l' anno in corso di un determinato studente


### POST /secretary/aula

parametri | descrizione
------------ | -------------
nome_sede | nome della sede dove è situata l' aula
numero_piano | numero del piano della sede dove è situata l' aula
numero_aula | numero dell' aula
capienza | numero delle persone che possono occupare l' intera aula

#### Response

Crea una nuuova aula in una determinata sede dell' università


### POST /secretary/cancella_aula

parametri | descrizione
------------ | -------------
nome_sede | nome della sede dove è situata l' aula
numero_piano | numero del piano della sede dove è situata l' aula
numero_aula | numero dell' aula

#### Response

Cancella una determinata aula di una determinata sede


### POST /secretary/cancella_corso_laurea

parametri | descrizione
------------ | -------------
codice_corso | codice del corso di laurea

#### Response

Cancella una determinato corso di laurea


### POST /secretary/cancella_disciplina

parametri | descrizione
------------ | -------------
codice_corso | codice del corso di laurea
codice_disciplina | codice di una disciplina

#### Response

Cancella una determinata determinata disciplina di un determinato corso di laurea


### POST /secretary/cancella_docente

parametri | descrizione
------------ | -------------
cf | codice fiscale di un professore
matricola_docente | matricola del docente

#### Response

Cancella un determinato professore dati la sua matricola ed il suo codice fiscale


### POST /secretary/cancella_insegnamento

parametri | descrizione
------------ | -------------
matricola_docente | matricola del docente
codice_corso | codice del corso di laurea
codice_disciplina | codice di una disciplina

#### Response

Cancella un determinato insegnamento di un determinato professore di un determinato corso di laurea


### POST /secretary/cancella_locazione

parametri | descrizione
------------ | -------------
nome_sede | nome della sede dove è situata l' aula
codice_corso | codice del corso di laurea

#### Response

Cancella la collocazione di un determinato corso di laurea in una determinata sede


### POST /secretary/cancella_sede

parametri | descrizione
------------ | -------------
nome_sede | nome della sede dove è situata l' aula

#### Response

Cancella una determinata sede universitaria


### POST /secretary/cancella_studente

parametri | descrizione
------------ | -------------
cf | codice fiscale di uno studente
matricola_studente | matricola_studente

#### Response

Cancella uno studente data la sua matricola ed il suo codice fiscale


### POST /secretary/contatto_sede

parametri | descrizione
------------ | -------------
nome_sede | nome della sede dove è situata l' aula
tipo_contatto | il tipo del contatto
valore_contatto | il valore del contatto

#### Response

Associa un determinato tipo di contatto con il suo valore ad una determinata sede


### POST /secretary/corso_laurea

parametri | descrizione
------------ | -------------
codice_corso | codice del corso di laurea
nome_corso | nome del corso di laurea
durata_corso_laurea | durata del corso di laurea

#### Response

Inserissce un nuovo corso di laurea


### GET /secretary/corso_laurea

#### Response

Restituisce tutti i corsi di laurea dell' università 


### POST /secretary/delete__contatto_persona

parametri | descrizione
------------ | -------------
cf | codice fiscale di una persona
tipo_contatto | il tipo del contatto
valore_contatto | il valore del contatto

#### Response

Cancella un determinato contatto di una determinata persona attraverso il suo codice fiscale


### POST /secretary/delete_lavora

parametri | descrizione
------------ | -------------
codice_corso | codice del corso di laurea
matricola_docente | matricola del docente

#### Response

Cancella il collegamento tra un determinato docente ed un determinato corso di laurea


### POST /secretary/disciplina

parametri | descrizione
------------ | -------------
codice_corso | codice del corso di laurea
codice_disciplina | codice della disciplina
nome_ disciplina | nome della disciplina
cfu | crediti formativi universitari della disciplina
semestre | semestre in cui viene svolta la disciplina
anno | anno in cui viene svolta la disciplina

#### Response

Inserisce una disciplina in un determinato corso di laurea nell' anno e nel semestre e con i cfu dati


### GET /secretary/disciplina

#### Response

Restituisce le discipline di tutti i corsi di laurea


### POST /secretary/docente

parametri | descrizione
------------ | -------------
cf | codice fiscale di un professore
nome | nome del docente
cognome | cognome docente
data_di_nascita | data di nascita del docente
luogo_di_nascita | luogo di nascita del docente
cap | codice di avviamento postale del docente
via_piazza | via del docente
civico | numero civico del docente
matricola_docente | matricola del docente
email_docente | email del docente
password_docente | password del docente

#### Response

Inserimento di un nuovo docente


### GET /secretary/docente

#### Response

Reperimento di tutti i docenti 


### POST /secretary/insegnamento

parametri | descrizione
------------ | -------------
matricola_docente | matricola del docente
codice_corso | codice del corso di laurea
codice_disciplina | codice della disciplina

#### Response

Collegamento di un docente all' insegnamento di una determinata disciplina di un determinato corso di laurea


### GET /secretary/insegnamento

#### Response

Reperimento di tutti gli insegnamenti 


### POST /secretary/insert_contatto_persona

parametri | descrizione
------------ | -------------
cf | codice fiscale di una persona
tipo_contatto | il tipo del contatto
valore_contatto | il valore del contatto

#### Response

Inserimento di un determinato tipo e valore contatto di una persona 


### POST /secretary/lavora

parametri | descrizione
------------ | -------------
codice_corso | codice del corso di laurea
matricola_docente | matricola del docente

#### Response

Collega un determinato docente ad un determinato corso di laurea


### POST /secretary/locazione

parametri | descrizione
------------ | -------------
nome_sede | nome della sede dove è situata l' aula
codice_corso | codice del corso di laurea

#### Response

Collega un determinato corso di laurea ad una determinata sede


### GET /secretary/locazione

#### Response

Reperimento di dove sono situati tutti i corsi di laurea


### POST /secretary/sede

parametri | descrizione
------------ | -------------
nome_sede | nome della sede dove è situata l' aula
orario_apertura | orario di apertura della sede
orario_chiusura | orario di chiusura della sede
numero_piani | numero dei piani della sede
cap | codice di avviamento postale della sede
via_piazza | via della sede
civico | civico della sede

#### Response

Collega un determinato corso di laurea ad una determinata sede


### GET /secretary/sede

#### Response

Reperimento di tutte le sedi


### POST /secretary/studente

parametri | descrizione
------------ | -------------
cf | codice fiscale di uno studente
nome | nome dello studente
cognome | cognome dello studente
data_di_nascita | data di nascita dello studente
luogo_di_nascita | luogo di nascita dello studente
cap | codice di avviamento postale dello studente
via_piazza | via dello studente
civico | numero civico dello studente
matricola_studente | matricola dello studente
email_studente | email dello studente
data_immatricolazione | data di immatricolazione dello studente
password_studente | password dello studente
codice_corso | codice del corso a cui si è iscritto lo studente

#### Response

Inserimento di un nuovo docente


### GET /secretary/studente

#### Response

Reperimento di tutti gli studenti


## Professor

### POST /professor/aggiorna_richiesta_ricevimento

parametri | descrizione
------------ | -------------
matricola_docente | matricola del docente
data_ricevimento | data ed orario del ricevimento del docente
matricola_studente | matricola dello studente
ora_inizio | orario inizio ricevimento
durata | durata del ricevimento

#### Response

Modifica di un determinato ricevimento tra docente e studente


### POST /professor/cancella_lezione

parametri | descrizione
------------ | -------------
codice_corso | codice del corso di laurea
codice_disciplina | codice della disciplina
nome_sede | nome della sede dove è situata l' aula
numero_piano | numero del piano della sede dove è situata l' aula
numero_aula | numero dell' aula
numero_lezione | numero della lezione

#### Response

Cancellazione di una lezione di una determinata disciplina di un determinato corso di laurea


### POST /professor/cancella_ricevimento

parametri | descrizione
------------ | -------------
matricola_docente | matricola del docente
data_ricevimento | data ed orario del ricevimento del docente

#### Response

Cancellazione di un determinato ricevimento


### POST /professor/inserimento_avviso

parametri | descrizione
------------ | -------------
matricola_docente | matricola del docente
codice_corso | codice del corso di laurea
codice_disciplina | codice della disciplina
data_avviso | data ed orario dell' avviso
titolo_avviso | titolo dell' avviso
corpo_avviso | corpo dell' avviso

#### Response

Inserimento/Creazione di un nuovo avviso


### POST /professor/inserimento_lezione

parametri | descrizione
------------ | -------------
codice_corso | codice del corso di laurea
codice_disciplina | codice della disciplina
nome_sede | nome della sede
numero_piano | numero del piano dell' aula
numero_aula | numero dell' aula
numero_lezione | numero della lezione
data_inizio | data ed orario di inizio della lezione
numero_ore | numero delle ora di lezione
titolo | titolo della lezione
descrizione | desscrizione della lezione

#### Response

Inserimento di una nuova lezione


### POST /professor/inserimento_ricevimento

parametri | descrizione
------------ | -------------
matricola_docente | matricola del docente
data_ricevimento | data ed orario del ricevimento del docente
ore_ricevimento | durata del ricevimento

#### Response

Inserimento di un nuovo ricevimento


### POST /professor/login

parametri | descrizione
------------ | -------------
matricola_docente | matricola del docente
password_docente | password docente

#### Response

Effettua il login del docente


### POST /professor/reperimento_avvisi

parametri | descrizione
------------ | -------------
matricola_docente | matricola del docente

#### Response

Reperimento di tutti gli avvisi del docente


### POST /professor/reperimento_insegnamenti

parametri | descrizione
------------ | -------------
matricola_docente | matricola del docente

#### Response

Reperimento di tutti gli insegnamenti del docente


### POST /professor/reperimento_lezioni

parametri | descrizione
------------ | -------------
matricola_docente | matricola del docente

#### Response

Reperimento di tutte le lezioni programmate dal docente


### POST /professor/reperimento_lista_studenti_iscritti_corso_piu_newsletter_per_chat

parametri | descrizione
------------ | -------------
matricola_docente | matricola del docente

#### Response

Reperimento di tutti gli studenti iscritti al corso ed agli avvisi del docente specificato


### POST /professor/reperimento_ricevimenti

parametri | descrizione
------------ | -------------
matricola_docente | matricola del docente

#### Response

Reperimento di tutti i ricevimenti programmati dal docente con le prenotazioni


### POST /professor/update_password

parametri | descrizione
------------ | -------------
nuova_password_docente | nuova password 
matricola_docente | matricola del docente
password_docente | vecchia password docente

#### Response

Variazione della password del docente


## Student

### POST /student/avvisi

parametri | descrizione
------------ | -------------
matricola_studente | matricola dello studente

#### Response

Reperimento avvisi delle discipline a cui lo sr


### POST /student/calendario

parametri | descrizione
------------ | -------------
matricola_studente | matricola dello studente

#### Response

Reperimento lezione delle discipline a cui lo studente è iscritto


### POST /student/cancella_richiesta_ricevimento

parametri | descrizione
------------ | -------------
matricola_docente | matricola del docente
data_ricevimento | data ed orario del ricevimento del docente
matricola_studente | matricola dello studente

#### Response

Cancellazione di una richiesta di uno specifico ricevimento


### POST /student/discipline_seguibili

parametri | descrizione
------------ | -------------
matricola_studente | matricola dello studente

#### Response

Reperimento discipline 


### POST /student/follow_disciplina

parametri | descrizione
------------ | -------------
codice_corso | codice corso di laurea
codice_disciplina | codice disciplina
matricola_studente | matricola dello studente

#### Response

Seguire una determinata disciplina di un determinato corso di laurea


### POST /student/iscrizione_newsletter

parametri | descrizione
------------ | -------------
codice_corso | codice corso di laurea
codice_disciplina | codice disciplina
matricola_studente | matricola dello studente

#### Response

Iscrizione agli avvisi di una determinata disciplina di un determinato corso di laurea


### POST /student/lista_prenotazioni_ricevimento

parametri | descrizione
------------ | -------------
matricola_studente | matricola dello studente

#### Response

Reperimento lista dei ricevimenti già prenotati dallo studente


### POST /student/lista_ricevimenti_prenotabili

parametri | descrizione
------------ | -------------
matricola_studente | matricola dello studente

#### Response

Reperimento lista dei ricevimenti prenotabili dallo studente


### POST /student/login

parametri | descrizione
------------ | -------------
matricola_studente | matricola del studente
password_studente | password studente

#### Response

Effettua il login dello studente


### POST /student/password

parametri | descrizione
------------ | -------------
nuova_password_studente | nuova password 
matricola_studente | matricola dello studente
password_studente | vecchia password studente

#### Response

Variazione della password dello studente


### POST /student/reperimento_lista_discipline_seguite

parametri | descrizione
------------ | -------------
matricola_studente | matricola dello studente

#### Response

Reperimento lista delle discipline seguite


### POST /student/reperimento_lista_docenti_iscrizione_corso_piu_newsletter_per_chat

parametri | descrizione
------------ | -------------
matricola_studente | matricola dello studente

#### Response

Reperimento lista docenti per la chat


### POST /student/reperimento_lista_iscrizioni_newsletter

parametri | descrizione
------------ | -------------
matricola_studente | matricola dello studente

#### Response

Reperimento lista per le iscrizioni agli avvisi


### POST /student/richiesta_ricevimento

parametri | descrizione
------------ | -------------
matricola_docente | matricola del docente
data_ricevimento | data ed orario del ricevimento del docente
matricola_studente | matricola dello studente
motivazione_ricevimento | motivazione per la quale si sta richiedendo un ricevimento con il docente

#### Response

Invio di una richiesta per un determinato ricevimento con motivazione


### POST /student/unfollow_disciplina

parametri | descrizione
------------ | -------------
codice_corso | codice corso di laurea
codice_disciplina | codice disciplina
matricola_studente | matricola dello studente

#### Response

Unfollow di una determinata disciplina di un determinato corso di laurea


### POST /student/unfollow_newsletter

parametri | descrizione
------------ | -------------
codice_corso | codice corso di laurea
codice_disciplina | codice disciplina
matricola_studente | matricola dello studente

#### Response

Unfollow degli avvisi di una determinata disciplina di un determinato corso di laurea


## Mongodb

### POST /mongodb/unfollow_newsletter

parametri | descrizione
------------ | -------------
matricola1 | matricola 
matricola2 | matricola

#### Response

Creazione di una nuova conversazione 


### POST /mongodb/get_all_colors

#### Response

Reperimento dei colori delle varie discipline


### POST /mongodb/get_all_conversations

parametri | descrizione
------------ | -------------
matricola | matricola 

#### Response

Reperimento di tutte le conversazioni 


### POST /mongodb/insert_discipline_color

parametri | descrizione
------------ | -------------
codice_corso | codice corso di laurea
codice_disciplina | codice disciplina
colore_esadecimale | colore in formato esadecimale

#### Response

Inserimento del colore di una determinata disciplina di un determinato corso di laurea


### POST /mongodb/send:message

parametri | descrizione
------------ | -------------
id_conversation | id della conversazione
matricola1 | matricola 
matricola2 | matricola
messaggio | messaggio di testo da inviare

#### Response

Invio del messaggio 


## Dependencies

```
aniso8601==8.0.0
appnope==0.1.0
astroid==2.4.1
attrs==19.3.0
backcall==0.1.0
bcrypt==3.1.7
cffi==1.14.0
click==7.1.2
decorator==4.4.2
dnspython==1.16.0
Flask==1.1.2
Flask-Bcrypt==0.7.1
Flask-Cors==3.0.8
flask-restx==0.2.0
Flask-SocketIO==4.3.0
gevent==20.5.2
gevent-websocket==0.10.1
greenlet==0.4.15
gunicorn==20.0.4
importlib-metadata==1.6.0
ipython==7.14.0
ipython-genutils==0.2.0
isort==4.3.21
itsdangerous==1.1.0
jedi==0.17.0
Jinja2==2.11.2
jsonschema==3.2.0
lazy-object-proxy==1.4.3
MarkupSafe==1.1.1
mccabe==0.6.1
mysql-connector-python==8.0.19
parso==0.7.0
pexpect==4.8.0
pickleshare==0.7.5
prompt-toolkit==3.0.5
protobuf==3.6.1
ptyprocess==0.6.0
pycparser==2.20
Pygments==2.6.1
pylint==2.5.2
pymongo==3.10.1
pyrsistent==0.16.0
python-dotenv==0.13.0
python-engineio==3.13.0
python-socketio==4.6.0
pytz==2020.1
scrypt==0.8.15
six==1.14.0
toml==0.10.1
traitlets==4.3.3
wcwidth==0.1.9
Werkzeug==1.0.1
wrapt==1.12.1
zipp==3.1.0
zope.event==4.4
zope.interface==5.1.0
```
