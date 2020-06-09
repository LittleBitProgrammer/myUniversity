// IMPORT LIB
import React from 'react';

// CREATE A COMPONENT
const RoundedImage = ({path,altText,className}) => {
    return <img src={path} alt={altText} className={`rounded${className ?' ' + className : ''}`}/>;
}

// EXPORT A COMPONENT
export default RoundedImage;