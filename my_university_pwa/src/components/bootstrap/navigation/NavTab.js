//IMPORT LIB
import React from 'react';
import { Link } from 'react-router-dom';

//CREATE COMPONENT 
const NavTab = ({isActive,id,to,tabName}) => {
    return (
        <li className="nav-item">
            <Link className={`nav-link ${isActive ? 'active' : ''}`} 
               id={id} 
               data-toggle='tab' 
               href={`#${to}`} 
               role='tab' 
               aria-controls={to}
               aria-selected={isActive}>{tabName}</Link>
        </li>
    );
}

//EXPORT A COMPONENT 
export default NavTab;