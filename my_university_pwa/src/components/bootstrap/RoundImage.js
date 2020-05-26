//import lib
import React from 'react';

//create a component 
const RoundImage = ({path, altText, width, height}) => {
    return (<img src={path} alt={altText} className='rounded-circle' width={width} height={height}/>);
}

RoundImage.defaultProps = {
    width:'75px',
    height:'75px'
}

//export a component 
export default RoundImage;