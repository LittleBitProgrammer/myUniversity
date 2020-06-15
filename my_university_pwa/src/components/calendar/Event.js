// This component is the custom component of the event in the calendar
//=====================================================================

// IMPORT LIB
import React from 'react';

// CREATE A COMPONENT
const Event = (props) => {
    return (
    <div className='event-component'>
        {props.value}
    </div>
    )
}

// EXPORT A COMPONENT
export default Event;