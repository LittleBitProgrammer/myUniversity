// IMPORT LIB
import React from 'react';

// CREATE A COMPONENT
const DropMenu = ({children,id}) => {
    return (
        <div class="dropdown-menu" aria-labelledby={id}>
            {children}
        </div>
    );
}

DropMenu.defaultProps({
    id: 'navbarDropdown'
})

// EXPORT A COMPONENT
export default DropMenu;