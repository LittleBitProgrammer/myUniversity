//import lib
import React from 'react';
import { NavLink } from 'react-router-dom';

//create a component 
const Brand = ({name, logoPath, width, height}) => {
    return (
        <NavLink className="navbar-brand" to="/">
            <img 
              src={logoPath} 
              width={width} 
              height={height} 
              className="d-inline-block align-top" 
              alt="my University logo" 
              loading="lazy"/>
            <span className='ml-3'>{name}</span>
        </NavLink>
    );
}

Brand.defaultProps = {
    width: 30,
    height: 30
}

//export a component 
export default Brand;