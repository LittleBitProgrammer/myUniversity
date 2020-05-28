//import lib
import React from 'react';

//create a component 
const Column = ({children,sizeColumnClass,className}) => {
    return <div className={sizeColumnClass}>{children}</div>
}

Column.defaultProps = {
    sizeScreen: 'col-md-4',
}

//export a component 
export default Column;