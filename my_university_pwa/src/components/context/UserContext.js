// IMPORT LIB
import React from 'react';
export const users = {
    student: {
        cf: '',
        nome: '',
        cognome: '',
        data_di_nascita: '',
        luogo_di_nascita: '',
        cap: 0,
        via_piazza: '',
        civico: '',
        matricola_studente: '',
        email_studente: '',
        data_immatricolazione: '',
        anno_in_corso: 0,
        contatti: []
    },
    teacher:{

    }
}
export const UserContext = React.createContext(users.student)