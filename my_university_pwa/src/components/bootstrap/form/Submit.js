//import lib
import React from 'react';

//create a component 
const Submit = ({buttontext,classColor, className,isLoading}) => {
    return (
    <button type='submit' className={`btn ${classColor} ${className}`} disabled={isLoading}>
    {isLoading && 
    <div>
        <span class="spinner-border spinner-border-sm text-light float-left mt-1" role="status" aria-hidden="true"></span>
        Caricando...
    </div>
    }
    {!isLoading &&<span className='text-center'>{buttontext}</span>}
    </button>
    );
}

Submit.defaultProps={
    buttontext: 'Submit',
    className: 'mt-3',
    isLoading: false
};

//export a component 
export default Submit;