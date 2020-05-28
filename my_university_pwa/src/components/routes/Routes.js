// IMPORT LIB
import React from 'react';
import {Switch} from 'react-router-dom';
// PAGES
import News from '../pages/News';
import Calendar from '../pages/Calendar';
import Receipt from '../pages/Receipt';
import Chat from '../pages/Chat';
import Profile from '../pages/Profile';
import Login from '../pages/Login';
import Navigation from '../navabar/Navigation';
import myUniversityLogo from '../../img/svg/graduation-hat.svg';
import NavRight from '../navabar/NavRight';
import NavLeft from '../navabar/NavLeft';
import Navitem from '../navabar/Navitem';
import RoundImage from '../bootstrap/RoundImage';
import AppRoute from '../AppRoute';

//create a component
const Routes = () => {
    return (
        <Switch>
            <AppRoute name="News" path="/" navBar={Navbar} component={News} exact/>
            <AppRoute name="Calendario" path="/calendario" navBar={Navbar} component={Calendar}/>
            <AppRoute name="Ricevimento" path="/ricevimento" navBar={Navbar} component={Receipt}/>
            <AppRoute name="Chat" path="/chat" navBar={Navbar} component={Chat}/>
            <AppRoute name="Profilo" path="/profilo" navBar={Navbar} component={Profile}/>
            <AppRoute name="Login" path="/login"  component={Login}/>
        </Switch>
    );
}

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
                    path='https://www.lascimmiapensa.com/wp-content/uploads/2019/03/Al-Bano-1.jpg' 
                    altText='profile image'
                    width='45px'
                    height='45px'/>
            </Navitem>
        </NavRight>
    </Navigation>
    )
}

//export a component 
export default Routes;