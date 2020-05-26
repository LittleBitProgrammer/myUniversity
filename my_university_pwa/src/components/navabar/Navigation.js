//import lib
import React from 'react';
import Toggler from './Toggler';
import Brand from './Brand';
import NavLeft from './NavLeft';
import NavRight from './NavRight';

// create a component 
const Navigation = ({brandName, className, children, width, height, logoPath}) => {
    return (
        <nav className={className}>
            <Brand name={brandName} logoPath={logoPath} width={width} height={height}/>
            <Toggler/>

            <div className="collapse navbar-collapse" id="navbarSupportedContent">
                <NavRight>
                    <li class="nav-item">
                        <a class="nav-link" href="/">Right</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/">Link</a>
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