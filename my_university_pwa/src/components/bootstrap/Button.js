//import lib
import React from 'react';

//create a component 
const Button = ({buttontext,classColor, className, onClick}) => {
    return <button className={`btn ${classColor} ${className}`} onClick={onClick}>{buttontext}</button>
}

Button.defaultProps={
    buttontext: 'Submit',
    onClick: function () {
        console.log('clicked');
    }

};

//export a component 
export default Button;