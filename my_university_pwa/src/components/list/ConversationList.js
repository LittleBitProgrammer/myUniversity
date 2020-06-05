// IMPORT LIB
import React from 'react';
import ConversationItem from "../items/ConversationItem";

// CREATE A COMPONENT
const ConversationList = ({messages}) => {
    const messageList = messages.map((message,index) => {

        return(<ConversationItem key={index} message={message} />)
    })
    return <div>{messageList}</div>;
}

// EXPORT A COMPONENT
export default ConversationList;