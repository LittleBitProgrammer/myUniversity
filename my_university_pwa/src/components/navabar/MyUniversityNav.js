// IMPORT LIB
import React from 'react';
import Navigation from './navigation/Navigation';
import myUniversityLogo from '../../img/svg/graduation-hat.svg';
import squareLogo from '../../img/svg/square-1.svg';
import NavRight from './navigation/NavRight';
import NavLeft from './navigation/NavLeft';
import Navitem from './navigation/Navitem';
import RoundImage from '../bootstrap/RoundImage';

// CREATE A COMPONENT
const Navbar = () => {
    return (
        <Navigation 
        className='navbar navbar-expand-lg navbar-dark bg-primary fixed-top' 
        brandName='myUniversity' 
        logoPath={myUniversityLogo}>
        <NavLeft>
            <Navitem path='/' name='News' exact={true}/>
            <Navitem path='/calendario' name='Calendario'/>
            <Navitem path='/ricevimento' name='Ricevimento'/>
            <Navitem path='/chat' name='Chat'/>
        </NavLeft>
        <NavRight>
            <Navitem path='/profilo'>
                <RoundImage 
                    path={squareLogo}
                    altText='profile image'
                    width='45px'
                    height='45px'
                    className='circle-border-white'
                    />
            </Navitem>
        </NavRight>
    </Navigation>
    )
}

//EXPORT A COMPONENT 
export default Navbar;