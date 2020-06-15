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
matricola1 | matricola primo interlocutore
matricola2 | matricola secondo interlocutore

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
matricola_mittente | matricola mittente
matricola_destinatario | matricola destinatario
messaggio | messaggio di testo da inviare

#### Response

Invio del messaggio 


## Dependencies

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