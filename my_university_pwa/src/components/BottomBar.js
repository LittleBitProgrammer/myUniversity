//import lib
import React from 'react';
import '../css/bottombar.css';

//create a component 
const BottomBar = ({firstYear, lastYear, authors}) => {
    let i = 0;
    const auths = authors.map((auth) => {
        if (i === 2){
            return (<span key={i++} className='text-primary'>{`${auth}`}</span>);
        }
        return (<span key={i++} className='text-primary'>{`${auth} - `}</span>);
    });

    return (
        <nav className='navbar navbar-expand navbar-light bg-light fixed-bottom'>
            <span className='navbar-text'>{`© Credits by ${firstYear}-${lastYear}`}</span>
            <span className='navbar-nav mr-auto'></span>
            <span className='navbar-text'>Developed by: {auths}</span>
        </nav>
    )
}

//export a component
export default BottomBar;