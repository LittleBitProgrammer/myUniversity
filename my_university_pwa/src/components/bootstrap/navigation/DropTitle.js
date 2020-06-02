// IMPORT LIB
import React from 'react';

// CREATE A COMPONENT 
const DropTitle = ({title,id}) => {
    return (
        <a 
          className='nav-link dropdown-toggle' 
          href='/' 
          id={id} 
          role='button' 
          data-toggle='dropdown' 
          aria-haspopup='true' 
          aria-expanded='false'>
          {title}
        </a>
    );
}

DropTitle.defaultProps = {
    title: 'Dropdown',
    id: 'navbarDropdown'
}

// EXPORT A COMPONENT
export default DropTitle;