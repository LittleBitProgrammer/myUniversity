//IMPORT LIB
import React from 'react';

// CREATE A COMPONENT 
const ProfileBody = ({children, className}) => {
    return (
        <div className={`d-flex flex-column ${className}`}>
            {children}
        </div>
    );
}

ProfileBody.defaultProps = {
    className: ''
}

// EXPORT A COMPONENT
export default ProfileBody;