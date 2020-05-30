//import lib
import React from 'react';

//create a component 
const RoundImage = ({path, altText, width, height, className, roundClass}) => {
    return (<img src={path} alt={altText} className={`${roundClass ? roundClass : 'rounded-circle'} ${className}`} width={width} height={height}/>);
}

RoundImage.defaultProps = {
    width:'75px',
    height:'75px'
}

//export a component 
export default RoundImage;