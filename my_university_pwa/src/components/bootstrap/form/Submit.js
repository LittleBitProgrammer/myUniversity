//import lib
import React from 'react';

//create a component 
const Submit = ({buttontext,classColor, className}) => {
    return <button type='submit' className={`btn ${classColor} ${className}`}>{buttontext}</button>
}

Submit.defaultProps={
    buttontext: 'Submit',
    className: 'mt-3'
};

//export a component 
export default Submit;