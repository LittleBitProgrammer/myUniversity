// IMPORT LIB
import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'

// CREATE A COMPONENT 
const DropTitle = ({title,id,logoImage}) => {
    return (
        <a 
          className='nav-link dropdown-toggle' 
          href='/' 
          id={id} 
          role='button' 
          data-toggle='dropdown' 
          aria-haspopup='true' 
          aria-expanded='false'>
          <span>{logoImage &&<FontAwesomeIcon icon={logoImage} className='mr-2'/>}{title}</span>
        </a>
    );
}

DropTitle.defaultProps = {
    title: 'Dropdown',
    id: 'navbarDropdown'
}

// EXPORT A COMPONENT
export default DropTitle;