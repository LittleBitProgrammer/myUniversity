//import lib
import React from 'react';

//create a component 
const CardImage = ({className, path, altText, style}) =>{
    return <img className={`card-img ${className}`} alt={altText} src={path} style={style}/>
}

//export a component 
export default CardImage;