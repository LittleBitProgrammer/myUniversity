//import lib
import React from 'react';

//create a component 
const CardTitle = ({children, className}) => {
    return <h5 className={`card-title ${className}`}>{children}</h5>;
}

//export a component 
export default CardTitle;