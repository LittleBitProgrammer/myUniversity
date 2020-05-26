//import lib
import React from 'react';
import {NavLink} from 'react-router-dom';
import Toggler from './Toggler';

// create a component 
const Navigation = ({brandName,className,children}) => {
    return (
        <nav className={className}>
            <NavLink className="navbar-brand" to="/">{brandName}</NavLink>
            <Toggler/>

            <div className="collapse navbar-collapse" id="navbarSupportedContent">
                <ul className="navbar-nav mr-auto">
                    {children}
                </ul>
            </div>
        </nav>
    );
}

Navigation.defaultProps = {
    brandName: 'Brand Name',
    className: 'navbar navbar-expand-lg  navbar-dark bg-primary'
}

// export a component 
export default Navigation;