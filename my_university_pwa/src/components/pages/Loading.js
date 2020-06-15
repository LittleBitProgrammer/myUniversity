// IMPORT LIB
import React from 'react';
// SVG
import logo from '../../img/svg/graduation-hat.svg';
// CSS
import '../../css/loading.css'

// CREATE A COMPONENT 
const Loading = (props) => {
    return (
        <div className='loading-background w-100'>
            <div className='container justify-content-center vertical-center h-100'>
                <div>
                    <img src={logo} alt='my university logo' className='loading-logo'/>
                    <h2 className='mb-5' id='loading-header'>My university</h2>
                </div>
                <div className="spinner-border text-white" style={{width: '4rem',height: '4rem'}} role="status">
                    <span className="sr-only">Loading...</span>
                </div>
                <div className='mt-4 text-white'>Autentificazione in corso attendere prego...</div>
            </div>
        </div>
    );
}

// EXPORT A COMPONENT 
export default Loading;