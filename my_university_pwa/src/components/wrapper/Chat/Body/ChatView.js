import React from "react";
import Card from "../../../bootstrap/Card/Card";
import ChatHeader from "./ChatHeader";

const chatCompose = (isDefault, nome, cognome)=>{
    if(!isDefault){
        return (<Card className='p-2'><ChatHeader/></Card>)
    }return(
        <Card className='p-2'><ChatHeader nome={nome} cognome={cognome}/></Card>
    )
}

const ChatVew = ({chats, chat_index})=>{
    if (chat_index){
        let chat = chats[chats.findIndex((obj)=>obj.id_conversation === chat_index)];
        return <Card className='p-2'>{`${chat.nome_docente} ${chat.cognome_docente}`}</Card>
    }
    return (<Card className='p-2'>{'Chat View'}</Card>)
}



ChatVew.defaultProps = {nome: '', cognome: ''}

export default ChatVew;