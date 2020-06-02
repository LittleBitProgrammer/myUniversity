// IMPORT LIB
import React from 'react';

// CREATE A COMPONENT 
const Contacts = ({phoneNumbers, emails}) => {
    
    const numberList = phoneNumbers.map((number,index) => {
        return <div key={index}><a href='/'>{number}</a></div>
    });

    const emailList = emails.map((email, index) => {
        return <div key={index}><a href='/'>{email}</a></div>
    });
   
    return (
        <div className='profile-contacts'>
            <p>Contatti Telefonici</p>
            {numberList}
            <p>Email</p>
            {emailList}
        </div>
    );
}

// EXPORT A COMPONENT 
export default Contacts;