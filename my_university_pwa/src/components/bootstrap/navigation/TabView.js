//IMPORT LIB
import React from 'react';

// CREATE A COMPONENT 
const TabView = ({children,className,animaationClass,isActive,id}) => {
    return (<div 
              className={`tab-pane ${animaationClass} ${isActive ? 'active show' : ''} ${className}`} 
              id={id}
              role='tabpanel'
              aria-labelledby={id}>
                {children}
            </div>);
}

TabView.defaultProps = {
    animaationClass: 'fade',
    isActive: false,
    className:''
}

// EXPORT A COMPONENT 
export default TabView;