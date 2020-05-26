// import lib
import React from 'react';

// create a component 
const Container = ({children}) => {
    return (
        <div className='container'>{children}</div>
    );
}

// export a component 
export default Container