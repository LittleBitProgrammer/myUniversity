// IMPORT LIB
import React from 'react'

// CREATE A COMPONENT 
const Toggler = ({onChange, checked}) => {
    return (
        <React.Fragment>
            <input 
            type="checkbox" 
            id="drawer-toggle" 
            name="drawer-toggle" 
            onChange={onChange} 
            checked={checked}/>
            <label htmlFor="drawer-toggle" id="drawer-toggle-label"></label>
        </React.Fragment>
    );
}

// EXPORT A COMPONENT 
export default Toggler;