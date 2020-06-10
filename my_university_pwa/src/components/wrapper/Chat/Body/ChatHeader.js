import React from "react";

const ChatHeader = ({nome, cognome})=>{
    return (
        <div className='bold-gray chat-header'>
            {nome && cognome ? `A: ${nome} ${cognome}`: 'Seleziona una chat'}
        </div>
    )
}
ChatHeader.defaultProps = {
    nome: "",
    cognome: ""
}
export default ChatHeader;