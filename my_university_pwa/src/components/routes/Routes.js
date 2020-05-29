// IMPORT LIB
import React, {Component} from 'react';
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
//CONTEXT
import {UserContext} from '../context/UserContext';

//create a component
class Routes extends Component {
    constructor(props){
        super(props)

        this.userType = this.props.userType;
        this.response = this.props.response;
    }

    componentDidMount(){
        console.log(this.userType);
        console.log(this.response)
        this.context.update({[this.userType]: this.response})
    }
    
    render(){
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
}

Routes.contextType = UserContext; 

//export a component 
export default Routes;