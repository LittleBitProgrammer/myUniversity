// IMPORT LIB
import React from "react";
import ChatItem from "../items/ChatItem";

// CREATE A COMPONENT
const ChatList = ({chats})=>{
    console.log('chats in chatlist',chats)
    const chatList = chats.map(
        (item) => {
            return (
                <ChatItem key={item.id_conversation}
                             fName={item.nome_docente}
                             sName={item.cognome_docente}
                             lastMessage={item.messages[item.messages.length - 1].messaggio}
                             lmTime={item.messages[item.messages.length - 1].data_invio}
                          lenght={chats.length}
                          index={item.id_conversation}
            />)
        }
    )
    return (
        <div>
            {chatList}
        </div>
    )
}

// EXPORT A COMPONENT
export default ChatList;