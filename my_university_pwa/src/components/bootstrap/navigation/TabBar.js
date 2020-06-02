// IMPORT LIB
import React from 'react';

//TODO:// Change in tabbar header

// CREATE A COMPONENT
const TabBar = ({children}) => {
    return (
        <ul className="nav nav-tabs" id="myTab" role="tablist">
            {children}
        </ul>
    );
}

export default TabBar;