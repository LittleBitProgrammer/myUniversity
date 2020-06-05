
// IMPORT LIB
import React from "react";
import Card from "../bootstrap/Card/Card";



// CREATE A COMPONENT

const ConversationItem = (message)=>{
    console.log(message)
    const mex = message.message;
    return (
        <Card>
            <p>{mex.messaggio}</p>
        </Card>
    )
}

// EXPORT A COMPONENT
export default ConversationItem;