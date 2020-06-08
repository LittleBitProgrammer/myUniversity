import React from "react";
import Column from "../../../bootstrap/Column";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faPaperPlane} from "@fortawesome/free-solid-svg-icons";
import Row from "../../../bootstrap/Row";
import ChatField from "../../../bootstrap/form/fields/ChatField";

//sizeTextSendButton serve ad impostare la garndezza del button
const ChatBottom = ({className,textCallback,maxRows,placeholder,sizeTextArea,sizeSendButton, sizeTextSendButton, onMessageSend, value})=>{
    return(
        <Row className={className}>

            <Column screenSize="lg" columnSize={sizeTextArea}>
                <ChatField
                    className="form-control"
                    maxRows={maxRows}
                    placeholder={placeholder}
                    textCallback={textCallback}
                    value={value}
                />

            </Column>
            <Column Column screenSize="lg" columnSize={sizeSendButton}>
                <FontAwesomeIcon icon={faPaperPlane} color='black' className="pointer toBottom" onClick={onMessageSend}/>
            </Column>
        </Row>
    )
}

export default ChatBottom;