import React from "react";
import Card from "../../../bootstrap/Card/Card";
import Button from "../../../bootstrap/Button";
import ChatList from "../../../list/ChatList";
import ScrollView from "../../../wrapper/ScrollView";


const SideChat = ({onButtonClick, chats, onItemClick})=>{
    return (
        <div>
            <Card className='p-2 sidechat-card-size'>
                <div>
                    <Button buttontext="Nuova Chat"
                            classColor="btn-primary"
                            onClick={onButtonClick}/>
                    <div>
                        <ScrollView>
                            <div>
                                <ChatList chats={chats}
                                          onItemClick={onItemClick}/>
                            </div>

                        </ScrollView>
                    </div>
                </div>
            </Card>
        </div>
    )
}

export default SideChat;