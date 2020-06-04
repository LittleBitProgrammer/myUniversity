// IMPORT LIB
import React from "react";
import squareLogo from "../../img/svg/Square-profile.svg"
import Row from "../bootstrap/Row";
import Column from "../bootstrap/Column";
import ChatImg from "../wrapper/Chat/ChatImage";
import {capitalizeFirstLetter,takeDate,takeTime, trimMessage} from "../../utility/functions";


// CREATE A COMPONENT

const ChatItem = ({fName, sName, lastMessage, lmTime, lenght, index})=>{

    return (
        <div className='mt-3 pointer pointed'>
            <Row className='no-gutters'>
                <Column columnSize='2' screenSize='lg'>
                    <ChatImg className='chat-profile-img mr-1' sigle={`${fName[0].toUpperCase().concat(sName[0].toUpperCase())}`} isVisibleInput={false} path={squareLogo}/>
                </Column>
                <Column columnSize='7' screenSize='lg' className='d-flex d-flex-column'>
                    <div className='ml-3'>
                        <div>{capitalizeFirstLetter(fName)} {capitalizeFirstLetter(sName)}</div>
                        <div className='text-muted'>{trimMessage(lastMessage)}</div>
                    </div>

                </Column>
                <Column className='d-flex d-flex-column' columnSize='3' screenSize='lg'>
                    <div>{takeTime(lmTime)}</div>
                    <div className='text-muted'>{takeDate(lmTime)}</div>
                </Column>
            </Row>
            {
                !(lenght === parseInt(index)) && <div className='dropdown-divider'></div>
            }

        </div>

    )
}

// EXPORT A COMPONENT
export default ChatItem;