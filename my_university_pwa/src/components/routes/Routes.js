// IMPORT LIB
import React, {Component} from 'react';
import {Switch, Redirect} from 'react-router-dom';
// PAGES
import News from '../pages/News';
import Calendar from '../pages/Calendar';
import Receipt from '../pages/Receipt';
import Chat from '../pages/Chat';
import Profile from '../pages/Profile';
import Login from '../pages/Login';
// ROUTING
import AppRoute from '../routing/AppRoute';
//COOKIE
import {Cookies} from 'react-cookie';

//create a component
class Routes extends Component {
    constructor(props){
        super(props)

        this.myCookies = new Cookies();
    }

    render(){
        return (
            <div>
                <Switch>
                <AppRoute name="News" path="/" component={News} {...this.props} exact>
                            {(this.myCookies.get('isAuth') === 'false' || this.myCookies.get('isAuth') === undefined) 
                            && <Redirect to={{pathname: "/login"}}/>}
                        </AppRoute>
                        <AppRoute name="Calendario" path="/calendario" component={Calendar} {...this.props} exact>
                            {(this.myCookies.get('isAuth') === 'false' || this.myCookies.get('isAuth') === undefined) 
                            && <Redirect to={{pathname: "/login"}}/>}
                        </AppRoute>
                        <AppRoute name="Ricevimento" path="/ricevimento" component={Receipt} {...this.props} exact>
                            {(this.myCookies.get('isAuth') === 'false' || this.myCookies.get('isAuth') === undefined) 
                            && <Redirect to={{pathname: "/login"}}/>}
                        </AppRoute>
                        <AppRoute name="Chat" path="/chat" component={Chat} {...this.props} exact>
                            {(this.myCookies.get('isAuth') === 'false' || this.myCookies.get('isAuth') === undefined) 
                            && <Redirect to={{pathname: "/login"}}/>}
                        </AppRoute>
                        <AppRoute name="Profilo" path="/profilo" component={Profile} {...this.props} exact>
                            {(this.myCookies.get('isAuth') === 'false' || this.myCookies.get('isAuth') === undefined) 
                            && <Redirect to={{pathname: "/login"}}/>}
                        </AppRoute>
                        <AppRoute name="Login" path="/login" component={Login} {...this.props} exact/>
                        <Redirect from='*' to='/'/>
                </Switch>
            </div>
        );
    }
}

//export a component 
export default Routes;