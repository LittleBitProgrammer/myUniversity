import React from "react";
import Button from "../../../bootstrap/Button";
import ChatList from "../../../list/ChatList";
import chatLogo from '../../../../img/svg/chat-add.svg';


const SideChat = ({onButtonClick, chats, onItemClick})=>{
    return (
        <div className='sidechat h-100 pr-4'>
            <Button 
              buttontext={
                <div>Nuova chat
                    <span className='ml-2'>
                        <img className='chat-logo' src={chatLogo} alt='chat add logo'/>
                    </span>
                </div>
                }
              classColor="btn-primary w-100"
              onClick={onButtonClick}/>
            <ChatList chats={chats} onItemClick={onItemClick}/>
        </div>
    )
}

export default SideChat;