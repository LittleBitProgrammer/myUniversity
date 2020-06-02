//import lib
import React, {Component} from 'react';
// LIST
import ChatList from '../list/ChatList';
//CONTEXT
import {UserContext} from '../context/UserContext';

//create a component
class Chat extends Component {



    render(){
        let matricola = this.context;
        return (
            <div>
                {console.log('prova',matricola)}
                <ChatList/>
            </div>
        );
    }
}
Chat.contextType = UserContext;

//export a component
export default Chat;