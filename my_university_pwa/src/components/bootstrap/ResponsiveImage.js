//import lib
import React from 'react';

//create a component
const ResponsiveImage = ({className, path, altText}) => {
    return <img className={`img-fluid ${className}`} src={path} alt={altText}/>;
}

//export a component 
export default ResponsiveImage;