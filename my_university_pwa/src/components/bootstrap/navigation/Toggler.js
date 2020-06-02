//import lib
import React from 'react';

//create a component 
const Toggler = () => {
    return (
        <button 
          className="navbar-toggler" 
          type="button" 
          data-toggle="collapse" 
          data-target="#navbarSupportedContent" 
          aria-controls="navbarSupportedContent"
          aria-expanded="false" 
          aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
        </button>
    );
}

// export a component 
export default Toggler;