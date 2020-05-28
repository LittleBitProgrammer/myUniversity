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
// ROUTING
import AppRoute from '../AppRoute';
// NAVBAR
import MyUniversityNav from '../navabar/MyUniversityNav'

//create a component
const Routes = () => {
    return (
        <Switch>
            <AppRoute name="News" path="/" navBar={MyUniversityNav} component={News} exact/>
            <AppRoute name="Calendario" path="/calendario" navBar={MyUniversityNav} component={Calendar}/>
            <AppRoute name="Ricevimento" path="/ricevimento" navBar={MyUniversityNav} component={Receipt}/>
            <AppRoute name="Chat" path="/chat" navBar={MyUniversityNav} component={Chat}/>
            <AppRoute name="Profilo" path="/profilo" navBar={MyUniversityNav} component={Profile}/>
            <AppRoute name="Login" path="/login"  component={Login}/>
        </Switch>
    );
}

//export a component 
export default Routes;