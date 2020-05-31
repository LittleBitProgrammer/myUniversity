// IMPORT LIB
import React from 'react';
import Navigation from './navigation/Navigation';
import myUniversityLogo from '../../img/svg/graduation-hat.svg';
import { faUser } from '@fortawesome/free-solid-svg-icons'
import NavRight from './navigation/NavRight';
import NavLeft from './navigation/NavLeft';
import Navitem from './navigation/Navitem';

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
            <Navitem path='/profilo' name='Profilo' logoImage={faUser}/>
        </NavRight>
    </Navigation>
    )
}

//EXPORT A COMPONENT 
export default Navbar;