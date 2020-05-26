//import lib
import React from 'react';
import { NavLink } from 'react-router-dom';
//NAVBAR
import Toggler from './Toggler';
import Brand from './Brand';
import NavLeft from './NavLeft';
import NavRight from './NavRight';
//BOOTSTRAP
import RoundImage from '../bootstrap/RoundImage';


// create a component 
const Navigation = ({brandName, className, children, width, height, logoPath}) => {
    return (
        <nav className={className}>
            <Brand name={brandName} logoPath={logoPath} width={width} height={height}/>
            <Toggler/>

            <div className="collapse navbar-collapse" id="navbarSupportedContent">
                <NavRight>
                    <li class="nav-item">
                        <NavLink class="nav-link" to="/profilo">
                            <RoundImage 
                              path='https://www.lascimmiapensa.com/wp-content/uploads/2019/03/Al-Bano-1.jpg' 
                              altText='profile image'
                              width='45px'
                              height='45px'
                              />
                        </NavLink>
                    </li>
                </NavRight>
                <NavLeft>
                    {children}
                </NavLeft>
                
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