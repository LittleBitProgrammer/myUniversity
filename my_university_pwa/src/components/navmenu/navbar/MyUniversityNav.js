// IMPORT LIB
import React from 'react';
// NAVIGATION
import Navigation from '../../bootstrap/navigation/Navigation';
import NavRight from '../../bootstrap/navigation/NavRight';
import NavLeft from '../../bootstrap/navigation/NavLeft';
import Navitem from '../../bootstrap/navigation/Navitem';
// DROPDOWN
import DropDown from '../../bootstrap/navigation/DropDown';
// IMAGES
import myUniversityLogo from '../../../img/svg/graduation-hat.svg';
import { faUser } from '@fortawesome/free-solid-svg-icons'
//CSS
import '../../../css/navbar.css';

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
            <DropDown title='Profilo' id='navbarDropdown' logoImage={faUser} className='dropdown-menu-right'>
                <a className="dropdown-item" href="/Profilo">Informazioni</a>
                <div className="dropdown-divider"></div>
                <a className="dropdown-item" href="/login">Esci</a>
            </DropDown>
        </NavRight>
    </Navigation>
    )
}

//EXPORT A COMPONENT 
export default Navbar;