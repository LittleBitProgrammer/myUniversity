//import lib
import React from 'react';

//create a component 
const Submit = ({onSubmitClick,buttontext,classColor, className}) => {
    return <button type='submit' className={`btn ${classColor} ${className}`} onClick={onSubmitClick}>{buttontext}</button>
}

Submit.defaultProps={
    buttontext: 'Submit',
    className: 'mt-3'
};

//export a component 
export default Submit;