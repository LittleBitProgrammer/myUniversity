//import lib
import React from 'react';

//create a component 
const NavRight = ({children}) => {

    return (
        <ul className={`navbar-nav ml-auto order-2`}>
            {children}       
        </ul>
    );
}

// export a component 
export default NavRight;