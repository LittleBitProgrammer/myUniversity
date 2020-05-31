//IMPORT LIB
import React from 'react';

// CREATE A COMPONENT 
const Sidebar = ({children}) => {
    return (
        <div class='d-flex flex-column'>
            {children}
        </div>
    );
}

// EXPORT A COMPONENT
export default Sidebar;