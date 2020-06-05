import React from "react";
import Card from "../../../bootstrap/Card/Card";
import ChatHeader from "./ChatHeader";
import TextArea from "../../../bootstrap/form/fields/TextArea";
import Row from "../../../bootstrap/Row";
import Column from "../../../bootstrap/Column";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faPaperPlane} from "@fortawesome/free-solid-svg-icons";
import ChatBottom from "./ChatBottom";

const ChatVew = ({chats, chat_index})=>{
    if (chat_index){
        let chat = chats[chats.findIndex((obj)=>obj.id_conversation === chat_index)];
        return (
            <Card className='p-2 chat-card-size'>
                <div className="d-flex-column maxHeight">
                    <Row>
                        <ChatHeader nome={chat.nome_docente} cognome={chat.cognome_docente}/>
                    </Row>

                    <ChatBottom
                        className="toBottom"
                        placeholder="Messaggio"
                        maxRows={4}
                        sizeSendButton="1"
                        sizeTextArea="11"
                        textCallback={ ()=>{console.log("button send value")}} />

                </div>

            </Card>)
    }
    return (<Card className='p-2 chat-card-size'><ChatHeader/></Card>)
}

export default ChatVew;