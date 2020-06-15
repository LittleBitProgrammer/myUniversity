// IMPORT LIB
import React from 'react';

// CREATE A COMPONENT 
const TabBody = ({children,className,id}) => {
    return <div className={`tab-content ${className}`} id={id}>{children}</div>
}

TabBody.defaultProps = {
    className: ''
}

// EXPORT A COMPONENT
export default TabBody;