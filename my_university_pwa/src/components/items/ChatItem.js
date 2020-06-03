// IMPORT LIB
import React from "react";
import ProfileImage from "../wrapper/ProfileImage";
import capitalizeFirstLetter from "../../utility/functions"
// CREATE A COMPONENT

const ChatItem = ({fName, sName, lastMessage, lmTime})=>{
    return (
        <div>
            <ProfileImage sigle={`${fName[0].toUpperCase()+ sName[0].toUpperCase()}`}/>

        </div>
    )
}

// EXPORT A COMPONENT
export default ChatItem;