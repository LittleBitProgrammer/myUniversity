//import lib
import React from 'react';
import {NavLink} from 'react-router-dom'

//create a component
const Navitem = ({path, name, exact}) => {
    return (
        <li className="nav-item active">
            <NavLink 
              className="nav-link" 
              to={path} 
              activeClassName='active'
              exact={exact}>
              {name}
              <span className="sr-only">(current)</span>
            </NavLink>
        </li>
    );
}

Navitem.defaultProps = {
    name: 'undefined',
    exact: 'false'
}

// export a component
export default Navitem;