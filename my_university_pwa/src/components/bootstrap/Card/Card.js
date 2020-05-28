//import lib
import React from 'react';

//create a component
const Card = ({children, className, maxWidth}) => {
    return (
        <div className={`card ${className}`} style={{maxWidth: maxWidth}}>
            {children}
        </div>
    );
 } 

Card.defaultProps={
    maxWith: '540px'
}

//export a component 
export default Card