// IMPORT LIB
import React, {Component} from 'react';
import ChatItem from "../modal/ModalItem";


// CREATE A COMPONENT
const ChatModalList = ({onButtonCLick})=>{
    return (
        <ChatItem onClick={() => { console.log("cliccato merda!") }} disciplineCode="0001" disciplineName="Analisi1" teacherName="Gioconda" teacherSName="Moscariello"/>
    )
}

// EXPORT A COMPONENT
export default ChatModalList;