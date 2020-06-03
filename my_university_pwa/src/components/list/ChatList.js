// IMPORT LIB
import React from "react";
import ChatItem from "../items/ChatItem";

// CREATE A COMPONENT
const ChatList = ({chats})=>{
    const chatList = chats.map(
        (item) => {
            return <ChatItem key={item.id_conversation} />
        }
    )
    return (
        <div>
            {chatList}
            {console.log(chats)}
        </div>
    )
}

// EXPORT A COMPONENT
export default ChatList;