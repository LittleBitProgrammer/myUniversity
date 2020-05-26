//import lib
import React from 'react';

//create a component
const Row = ({className, children}) =>{
    return (<div className={`row ${className}`}>{children}</div>);
}

//export a component 
export default Row;