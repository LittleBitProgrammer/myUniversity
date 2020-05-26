//import lib
import React from 'react';

//create a component 
const NavLeft = ({children}) => {
    return (
        <ul className="navbar-nav mr-auto">
            {children}
        </ul>
    );
}

//export a component 
export default NavLeft;