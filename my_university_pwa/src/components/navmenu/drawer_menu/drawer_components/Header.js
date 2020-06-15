// IMPORT LIB
import React from 'react';

// CREATE A COMPONENT
const Header = ({logo,text,logoClass,altText}) => {
    return (
        <header>
            {text}
            <img src={logo} alt={altText} className={logoClass}/>
        </header>
    );
}

// EXPORT A COMPONENT 
export default Header;