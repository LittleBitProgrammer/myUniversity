//IMPORT LIB
import React from 'react';

//CREATE COMPONENT 
const NavTab = ({isActive}) => {
    return (
        <li className="nav-item">
            <a className={`nav-link ${isActive ? 'active' : ''}`} id="home-tab" data-toggle="tab" href="#home" role="tab" aria-controls="home" aria-selected="true">Informazioni</a>
        </li>
    );
}

//EXPORT A COMPONENT 
export default NavTab;