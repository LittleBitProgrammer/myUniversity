import React from "react";

const ChatHeader = ({nome, cognome})=>{
    return (
        <div>
            {nome && cognome ? `${nome} ${cognome}`: "Chat View"}
        </div>
    )
}
ChatHeader.defaultProps = {
    nome: "",
    cognome: ""
}
export default ChatHeader;