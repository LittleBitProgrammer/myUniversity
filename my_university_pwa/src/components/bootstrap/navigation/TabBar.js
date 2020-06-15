// IMPORT LIB
import React from 'react';


// CREATE A COMPONENT
const TabBar = ({children,className}) => {
    return (
        <div className={className}>
            {children}
        </div>
    );
}

TabBar.defaultProps = {
    className: ''
}

export default TabBar;