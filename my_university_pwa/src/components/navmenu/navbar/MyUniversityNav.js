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
//COOKIE
import {Cookies} from 'react-cookie';
//CSS
import '../../../css/navbar.css';
import { Link } from 'react-router-dom';

const logout = () => {
    const cookies = new Cookies();

    cookies.remove('isAuth');
    cookies.remove('matricola_studente');
    cookies.remove('password_studente');
    cookies.remove('userCookies');
}

// CREATE A COMPONENT
const Navbar = () => {
    const cookies = new Cookies();
    console.log(cookies.getAll())
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
                <Link className="dropdown-item" to="/Profilo">Informazioni</Link>
                <div className="dropdown-divider"></div>
                <a className="dropdown-item" href="/login" onClick={logout}>Esci</a>
            </DropDown>
        </NavRight>
    </Navigation>
    )
}

//EXPORT A COMPONENT 
export default Navbar;