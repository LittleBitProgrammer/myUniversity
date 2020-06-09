// IMPORT LIB
import React from 'react';
import ChatModalItem from "../items/ChatModalItem";


// CREATE A COMPONENT
const ChatModalList = ({onModalItemCLick, contacts})=>{

    console.log('contatti in lista cos',contacts);
    if(!contacts){
        return (
            <div>
                Empty
            </div>
        )
    }
    const contactList = contacts.map( (contact, index) => {
        return (
            <ChatModalItem key={index}
                           onClick={onModalItemCLick}
                           disciplineCode={contact.codice_disciplina}
                           disciplineName={contact.nome_disciplina}
                           teacherName={contact.nome}
                           teacherSName={contact.cognome}
                           matricolaDocente={contact.matricola_docente}
            />
        )
    });
    return (
        <div>
            {contactList}
        </div>
    )
}

// EXPORT A COMPONENT
export default ChatModalList;