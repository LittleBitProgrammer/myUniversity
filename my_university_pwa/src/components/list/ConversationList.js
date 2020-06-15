// IMPORT LIB
import React from 'react';
import ConversationItem from '../items/ConversationItem';
import {takeTime} from '../../Utility/functions'

// CREATE A COMPONENT
const ConversationList = ({messages,freshman}) => {
    const messageList = messages.map((message,index) => {

        return(
            <ConversationItem 
              key={index} 
              message={message.messaggio} 
              time={takeTime(message.data_invio)}
              isUserLogin={freshman === message.matricola_mittente}
              />
        )
    })
    return <div className='conv-list'>{messageList}</div>;
}

// EXPORT A COMPONENT
export default ConversationList;