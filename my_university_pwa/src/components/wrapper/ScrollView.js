import React from 'react';

//create a component
const ScrollView = ({children, className}) => {
    return(<div style={{height: '100%', overflowY: 'scroll'}} className={className?className:""}>
        {children}
    </div>)
}

//export a component
export default ScrollView;