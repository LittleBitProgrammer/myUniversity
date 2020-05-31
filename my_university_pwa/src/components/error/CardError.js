// IMPORT LIB
import React from 'react';
// CARD
import Card from '../bootstrap/Card/Card';

// CREATE A COMPONENT
const CardError = ({errorMessage}) => {
    return (
        <Card className='mt-3 bg-danger'>
            <ul className="list-group list-group-flush">
                <li className='list-group-item text-danger'>{errorMessage}</li>
            </ul>
        </Card>
    );
}

// IF CARD ERROR DOES NOT HAVE AN ERROR MESSAGE SET TO DEFAULT
CardError.defaultProps = {
    errorMessage: 'There was an error'
}

// EXPORT A COMPONENT 
export default CardError;