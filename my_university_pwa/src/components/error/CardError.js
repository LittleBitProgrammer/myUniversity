// IMPORT LIB
import React from 'react';

// CREATE A COMPONENT
const CardError = ({errorMessage}) => {
    return (
        <div className="alert alert-danger mt-3" role="alert">
            {errorMessage}
        </div>
    );
}

// IF CARD ERROR DOES NOT HAVE AN ERROR MESSAGE SET TO DEFAULT
CardError.defaultProps = {
    errorMessage: 'There was an error'
}

// EXPORT A COMPONENT 
export default CardError;