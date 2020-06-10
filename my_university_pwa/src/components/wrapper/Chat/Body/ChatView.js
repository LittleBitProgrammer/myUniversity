import React from "react";
import ChatHeader from "./ChatHeader";
import Row from "../../../bootstrap/Row";
import ChatBottom from "./ChatBottom";
import ConversationList from "../../../list/ConversationList";
import ScrollView from "../../ScrollView";

const ChatVew = ({chats, chat_index, onInputChange, onMessageSend, value, freshman})=>{
    if (chat_index){
        let chat = chats[chats.findIndex((obj)=>obj.id_conversation === chat_index)];
        return (
                <div className="maxHeight chat-container">
                    <Row>
                        <ChatHeader nome={chat.nome_docente} cognome={chat.cognome_docente}/>
                    </Row>
                    <ScrollView>
                        <ConversationList messages={chat.messages} freshman={freshman}/>
                    </ScrollView>

                    <ChatBottom
                        className="float-bottom no-gutters"
                        placeholder="Messaggio"
                        maxRows={4}
                        sizeSendButton="1"
                        sizeTextArea="11"
                        textCallback={onInputChange}
                        onMessageSend={onMessageSend}
                        value={value}
                    />
                </div>)
    }
    return (<div className='p-2 chat-card-size'><ChatHeader/></div>)
}

export default ChatVew;