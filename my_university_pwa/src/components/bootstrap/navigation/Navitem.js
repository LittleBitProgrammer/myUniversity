//import lib
import React from 'react';
import {NavLink} from 'react-router-dom'


//create a component
const Navitem = ({path, name, exact,logoImage,className,liClass,onClick,children}) => {
    return (
        <li className={liClass}>
            <NavLink 
              className={`nav-link${className?' ' + className : ''}`}
              to={path} 
              exact={exact}
              onClick={onClick}
              activeClassName='my-university-active'>
              <span>{logoImage &&<img src={logoImage} className='mr-2' alt='icon menu'/>}{name}</span>
            {children}
              <span className="sr-only">(current)</span>
            </NavLink>
        </li>
    );
}

Navitem.defaultProps = {
    name: '',
    exact: false
}

// export a component
export default Navitem;