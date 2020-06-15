// This component is the custom component of the event in the calendar
//=====================================================================

// IMPORT LIB
import React from 'react';

// CREATE A COMPONENT
const Event = (props) => {
    return (
    <div className='event-component' style={{backgroundColor: props.color}}>
        {props.value}
    </div>
    )
}

Event.defaultProps = {
    color: '#0165d1'
}

// EXPORT A COMPONENT
export default Event;