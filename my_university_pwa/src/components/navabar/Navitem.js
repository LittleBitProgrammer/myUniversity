//import lib
import React from 'react';
import {NavLink} from 'react-router-dom'

//create a component
const Navitem = ({path, name, exact}) => {
    return (
        <li className="nav-item" data-toggle='collapse' data-target='.navbar-collapse.show'>
            <NavLink 
              className="nav-link" 
              to={path} 
              exact={exact}
              activeClassName='active'>
              {name}
              <span className="sr-only">(current)</span>
            </NavLink>
        </li>
    );
}

Navitem.defaultProps = {
    name: 'undefined',
    exact: false
}

// export a component
export default Navitem;