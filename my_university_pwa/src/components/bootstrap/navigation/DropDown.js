// IMPORT LIB
import React from 'react';
import DropTitle from '../navigation/DropTitle';
import DropMenu from '../navigation/DropMenu';

// CREATE A COMPONENT 
const DropDown = ({children,className,id,title,logoImage}) => {
    return (
        <li className={`nav-item dropdown ${className ? className : ''}`}>
            <DropTitle id={id} title={title} logoImage={logoImage}/>
            <DropMenu id={id}>
                {children}
            </DropMenu>
        </li>
    );
}

DropDown.defaultProps = {
    id: 'navbarDropdown',
    title: 'DropMenu'
}

// EXPORT A COMPONENT
export default DropDown;