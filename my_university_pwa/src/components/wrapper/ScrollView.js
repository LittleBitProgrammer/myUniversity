import React from 'react';

//create a component
const ScrollView = ({children}) => {
    return(<div style={{height: '100%', overflowY: 'scroll'}}>
        {children}
    </div>)
}

//export a component
export default ScrollView;