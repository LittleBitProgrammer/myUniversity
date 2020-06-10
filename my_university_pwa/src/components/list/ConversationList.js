// IMPORT LIB
import React from 'react';
import ConversationItem from '../items/ConversationItem';
import {takeTime} from '../../utility/functions'

// CREATE A COMPONENT
const ConversationList = ({messages}) => {
    const messageList = messages.map((message,index) => {
        console.log(message);

        return(
            <ConversationItem 
              key={index} 
              message={message.messaggio} 
              time={takeTime(message.data_invio)}/>
        )
    })
    return <div>{messageList}</div>;
}

// EXPORT A COMPONENT
export default ConversationList;