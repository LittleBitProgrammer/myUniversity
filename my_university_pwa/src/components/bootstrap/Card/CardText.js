// IMPORT LIB
import React from 'react';

// CREATE A COMPONENT 
const CardText = ({children, className}) => {
    return (
        <p className={`card-subtitle mb-2 text-muted ${className ? className : null}`}>{children}</p>
    );
}

// EXPORT A COMPONENT 
export default CardText;