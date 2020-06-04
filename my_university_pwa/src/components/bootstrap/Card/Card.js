//import lib
import React from 'react';

//create a component
const Card = ({children, className, maxWidth, onClick}) => {
    return (
        <div className={`card ${className}`} style={{maxWidth: maxWidth}} onClick={onClick}>
            {children}
        </div>
    );
 } 

Card.defaultProps={
    maxWith: '540px'
}

//export a component 
export default Card