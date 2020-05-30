//import lib
import React from 'react';

//create a component 
const Column = ({children,screnSize,columnSize,className}) => {
    return <div className={`col-${screnSize}-${columnSize} ${className}`}>{children}</div>
}

Column.defaultProps = {
    sizeScreen: 'col-md-4',
}

//export a component 
export default Column;