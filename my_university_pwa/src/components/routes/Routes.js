// import lib
import React from 'react';
import {Route ,Switch} from 'react-router-dom';
// PAGES
import News from '../pages/News';
import Calendar from '../pages/Calendar';
import Receipt from '../pages/Receipt';
import Chat from '../pages/Chat';
import Profile from '../pages/Profile';

//create a component
const Routes = () => {
    return (
        <Switch>
            <Route path='/' component={News} exact/>
            <Route path='/calendario' component={Calendar}/>
            <Route path='/ricevimento' component={Receipt}/>
            <Route path='/chat' component={Chat}/>
            <Route path='/profilo' component={Profile}/>
        </Switch>
    );
}

//export a component 
export default Routes;