// IMPORT LIB
import React from "react";
import squareLogo from "../../img/svg/square.svg"
import Row from "../bootstrap/Row";
import Column from "../bootstrap/Column";
import {capitalizeFirstLetter,takeDate, trimMessage} from "../../utility/functions";
import ProfileImage from "../wrapper/ProfileImage";


// CREATE A COMPONENT

const ChatItem = ({fName, sName, lastMessage, lmTime, lenght, index, onItemClick})=>{

    return (
        <li className='person pt-3 pb-3' onClick={() => {onItemClick(index)}}>
            <Row className='no-gutters'>
                <Column columnSize='2'>
                    <ProfileImage 
                      className='chat-user'
                      containerClass='mt-0'
                      sigle={`${fName[0].toUpperCase().concat(sName[0].toUpperCase())}`} 
                      path={squareLogo}/>
                </Column>
                <Column columnSize='7' screenSize='lg'>
                    <div className='ml-3'>
                        <div className='chat-name'>{capitalizeFirstLetter(fName)} {capitalizeFirstLetter(sName)}</div>
                        <div className='text-muted'>{trimMessage(lastMessage)}</div>
                    </div>

                </Column>
                <Column columnSize='3'>
                    <div className='light-gray chat-date'>{takeDate(lmTime)}</div>
                </Column>
            </Row>

        </li>

    )
}

// EXPORT A COMPONENT
export default ChatItem;