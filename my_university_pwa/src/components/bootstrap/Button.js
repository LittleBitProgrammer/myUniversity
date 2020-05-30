//import lib
import React from 'react';

//create a component 
const Button = ({buttontext,classColor, className}) => {
    return <button className={`btn ${classColor} ${className}`}>{buttontext}</button>
}

Button.defaultProps={
    buttontext: 'Submit'
};

//export a component 
export default Button;