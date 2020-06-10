import React from "react";
import Column from "../../../bootstrap/Column";
import Row from "../../../bootstrap/Row";
import ChatField from "../../../bootstrap/form/fields/ChatField";
import send from '../../../../img/svg/send.svg';

//sizeTextSendButton serve ad impostare la garndezza del button
const ChatBottom = ({className,textCallback,maxRows,placeholder,sizeTextArea,sizeSendButton, sizeTextSendButton, onMessageSend, value})=>{
    return(
        <Row className={className}>

            <Column columnSize={sizeTextArea}>
                <ChatField
                    className="form-control chat-area"
                    maxRows={maxRows}
                    placeholder={placeholder}
                    textCallback={textCallback}
                    value={value}
                />

            </Column>
            <Column columnSize={sizeSendButton}>
                <img src={send} className="float-bottom send-logo" alt='Send button' onClick={onMessageSend}/>
            </Column>
        </Row>
    )
}

export default ChatBottom;