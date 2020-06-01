//import lib
import React from 'react';
import {NavLink} from 'react-router-dom'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'

//TODO: create component icon with text

//create a component
const Navitem = ({path, name, exact,logoImage, children}) => {
    return (
        <li className="nav-item" data-toggle='collapse' data-target='.navbar-collapse.show'>
            <NavLink 
              className="nav-link" 
              to={path} 
              exact={exact}
              activeClassName='active'>
              <span>{logoImage &&<FontAwesomeIcon icon={logoImage} className='mr-2'/>}{name}</span>
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