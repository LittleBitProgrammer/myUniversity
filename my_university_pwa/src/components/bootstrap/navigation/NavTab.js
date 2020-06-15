//IMPORT LIB
import React from 'react';

//CREATE COMPONENT 
const NavTab = ({isActive,id,to,tabName}) => {
    return (
        <li className="nav-item">
            <a className={`nav-link ${isActive ? 'active show' : ''}`} 
               id={id} 
               data-toggle='tab' 
               href={`#${to}`} 
               role='tab' 
               aria-controls={id}
               aria-selected={isActive}>{tabName}</a>
        </li>
    );
}

//EXPORT A COMPONENT 
export default NavTab;