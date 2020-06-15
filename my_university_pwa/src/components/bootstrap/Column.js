//import lib
import React from 'react';

//create a component 
const Column = ({children,screenSize,columnSize,className}) => {
    return <div className={`${screenSize ? 'col-' + screenSize + '-' + columnSize : 'col-' + columnSize}${className ? ' ' + className : ''}`}>{children}</div>
}

//export a component 
export default Column;