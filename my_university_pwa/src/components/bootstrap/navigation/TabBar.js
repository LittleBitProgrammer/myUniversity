// IMPORT LIB
import React from 'react';

//TODO:// Change in tabbar header

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