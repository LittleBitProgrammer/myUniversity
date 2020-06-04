// IMPORT LIB
import React, {Component} from 'react';

// CREATE A COMPONENT
const ChatItem = ({onClick, disciplineCode, disciplineName, teacherSName, teacherName})=>{
    return (
        <div className="pointer pt-3 pb-3" onClick={onClick}>
            <p className="h6"> {`${disciplineCode} - ${disciplineName} - ${teacherSName}  ${teacherName}`}</p>
        </div>
    )
}

// EXPORT A COMPONENT
export default ChatItem;