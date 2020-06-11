// IMPORT LIB
import React from 'react';

// CREATE A COMPONENT 
const HeaderCalendar = ({year,courseName,semester}) => {
    return (
        <div className='text-center calendar-header'>
            {`A.A. ${parseInt(year)-1}/${year} - ${semester}`}<br/>
            <span>{courseName}</span>
        </div>
    )
}

HeaderCalendar.defaultProps = {
    courseName: 'Informatica'
}

// EXPORT A COMPONENT
export default HeaderCalendar;