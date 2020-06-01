// IMPORT LIB
import React from 'react';

// CREATE A COMPONENT
const RoundedImage = ({path,altText}) => {
    return <img src={path} alt={altText} className='rounded'/>;
}

// EXPORT A COMPONENT
export default RoundedImage;