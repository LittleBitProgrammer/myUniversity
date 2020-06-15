// IMPORT LIB
import React from "react";
import ChatItem from "../items/ChatItem";

// CREATE A COMPONENT
const ChatList = ({chats, onItemClick})=>{
    const chatList = chats.map(
        (item) => {
            let messaggio = "inizia una nuova conversazione";
            let lmTime = "                ";
            if(item.messages.length !== 0){
                messaggio = item.messages[item.messages.length - 1].messaggio;
                lmTime = item.messages[item.messages.length - 1].data_invio;
            }

            return (
                    <ChatItem key={item.id_conversation}
                              fName={item.nome_docente}
                              sName={item.cognome_docente}
                              lastMessage={messaggio}
                              lmTime={lmTime}
                              lenght={chats.length}
                              index={item.id_conversation}
                              onItemClick={onItemClick}
                    />
            )
        }
    )
    return (
        <ul className="users mt-3 chat-list">
            {chatList}
        </ul>
    )
}

// EXPORT A COMPONENT
export default ChatList;