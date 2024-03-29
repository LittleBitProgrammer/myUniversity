
// IMPORT LIB
import React from "react";


// CREATE A COMPONENT

const ConversationItem = ({message,isUserLogin})=>{
    return (
        <div>
            <p className={isUserLogin ? 'chat-right' : 'chat-left'}>{message}</p>
        </div>
    )
}

// EXPORT A COMPONENT
export default ConversationItem;