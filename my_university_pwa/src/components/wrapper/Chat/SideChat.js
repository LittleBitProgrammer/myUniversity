import React from "react";
import Card from "../../bootstrap/Card/Card";
import Button from "../../bootstrap/Button";
import ChatList from "../../list/ChatList";



const SideChat = ({onButtonCLick, chats})=>{
    return (
        <div>
            <Card className='p-2'>
                <Button buttontext="Nuova Chat" classColor="btn-primary" onClick={onButtonCLick}/>
                <ChatList chats={chats}/>
            </Card>
        </div>
    )
}

export default SideChat;