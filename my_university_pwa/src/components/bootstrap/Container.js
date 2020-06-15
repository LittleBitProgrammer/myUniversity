// import lib
import React from 'react';

// create a component 
const Container = ({children, className}) => {
    return (
        <div className={`container${className? ' ' + className : ''}`}>{children}</div>
    );
}

// export a component 
export default Container