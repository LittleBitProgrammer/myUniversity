// IMPORT LIB
import React from 'react';
import Row from '../../bootstrap/Row';
import Column from '../../bootstrap/Column';
import mail from '../../../img/svg/mail.svg';
import phone from '../../../img/svg/phone.svg';

// CREATE A COMPONENT 
const Contacts = ({phoneNumbers, emails}) => {
    
    const numberList = phoneNumbers.map((number,index) => {
        return <div key={index}><a href='/'>{number}</a></div>
    });

    const emailList = emails.map((email, index) => {
        return <div key={index}><a href='/'>{email}</a></div>
    });
   
    return (
        <Row className='no-gutters'>
            <Column columnSize='6'>
                <div className='profile-contacts'>
                    <p><span><img src={phone} alt='mail logo' className='mb-2 mr-1'/></span>Telefono</p>
                    {numberList}
                </div>
            </Column>
            <Column columnSize='6'>
                <div className='profile-contacts'>
                    <p><span><img src={mail} alt='mail logo' className='mb-1 mr-1'/></span>Email</p>
                    {emailList}
                </div>
            </Column>  
        </Row>
    );
}

// EXPORT A COMPONENT 
export default Contacts;