// IMPORT LIB
import React, {Component} from 'react';
import ChatItem from "../modal/ModalItem";


// CREATE A COMPONENT
const ChatModalList = ({onButtonCLick, contacts})=>{

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
            <ChatItem key={index}
                          onClick={onButtonCLick}
                      disciplineCode={contact.codice_disciplina}
                      disciplineName={contact.nome_disciplina}
                      teacherName={contact.nome}
                      teacherSName={contact.cognome}/>
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