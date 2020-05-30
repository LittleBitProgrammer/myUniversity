//import lib
import React from 'react';
//NAVBAR
import Toggler from './Toggler';
import Brand from './Brand';


// create a component 
const Navigation = ({brandName, className, children, width, height, logoPath}) => {
    return (
        <nav className={className}>
            <Brand name={brandName} logoPath={logoPath} width={width} height={height}/>
            <Toggler/>

            <div className="collapse navbar-collapse" id="navbarSupportedContent">
                {children}
            </div>
        </nav>
    );
}

Navigation.defaultProps = {
    brandName: 'Brand Name',
    className: 'navbar navbar-expand-lg navbar-dark bg-primary'
}

// export a component 
export default Navigation;