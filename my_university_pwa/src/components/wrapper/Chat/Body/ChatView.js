import React from "react";
import Card from "../../../bootstrap/Card/Card";
import ChatHeader from "./ChatHeader";
import Row from "../../../bootstrap/Row";
import ChatBottom from "./ChatBottom";
import ConversationList from "../../../list/ConversationList";
import ScrollView from "../../ScrollView";

const ChatVew = ({chats, chat_index, onInputChange, onMessageSend})=>{
    if (chat_index){
        let chat = chats[chats.findIndex((obj)=>obj.id_conversation === chat_index)];
        return (
            <Card className='p-2 chat-card-size'>
                <div className="d-flex-column maxHeight">
                    <Row>
                        <ChatHeader nome={chat.nome_docente} cognome={chat.cognome_docente}/>
                    </Row>
                    <ScrollView>
                        <ConversationList messages={chat.messages}/>
                    </ScrollView>

                    <ChatBottom
                        className="toBottom"
                        placeholder="Messaggio"
                        maxRows={4}
                        sizeSendButton="1"
                        sizeTextArea="11"
                        textCallback={onInputChange}
                        onMessageSend={onMessageSend}
                    />
                </div>
            </Card>)
    }
    return (<Card className='p-2 chat-card-size'><ChatHeader/></Card>)
}

export default ChatVew;