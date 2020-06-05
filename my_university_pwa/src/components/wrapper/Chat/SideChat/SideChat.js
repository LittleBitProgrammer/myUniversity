import React from "react";
import Card from "../../../bootstrap/Card/Card";
import Button from "../../../bootstrap/Button";
import ChatList from "../../../list/ChatList";



const SideChat = ({onButtonClick, chats, onItemClick})=>{
    return (
        <div>
            <Card className='p-2'>
                <Button buttontext="Nuova Chat"
                        classColor="btn-primary"
                        onClick={onButtonClick}/>
                <ChatList chats={chats}
                          onItemClick={onItemClick}/>
            </Card>
        </div>
    )
}

export default SideChat;