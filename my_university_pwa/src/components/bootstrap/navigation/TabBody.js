// IMPORT LIB
import React from 'react';

// CREATE A COMPONENT 
const TabBody = ({children,id}) => {
    return <div className='tab-content' id={id}>{children}</div>
}

// EXPORT A COMPONENT
export default TabBody;