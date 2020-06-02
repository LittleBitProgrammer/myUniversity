// IMPORT LIB
import React from 'react';
import DropTitle from '../navigation/DropTitle';
import DropMenu from '../navigation/DropMenu';

// CREATE A COMPONENT 
const DropDown = ({children,id}) => {
    return (
        <div class='nav-item dropdown'>
            <DropTitle id={id} title='Profilo'/>
            <DropMenu id={id}>
                {children}
            </DropMenu>
        </div>
    );
}

DropDown.defaultProps = {
    id: 'navbarDropdown'
}

// EXPORT A COMPONENT
export default DropMenu;