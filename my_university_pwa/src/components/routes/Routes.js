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
// NAVBAR
import MyUniversityNav from '../navmenu/navbar/MyUniversityNav';
//CONTEXT
import {UserContext} from '../context/UserContext';
//AXIOS
import myUniversity from '../../API/myUniversity';
//COOKIE
import {Cookies, withCookies} from 'react-cookie';
import {instanceOf} from 'prop-types';

//create a component
class Routes extends Component {
    static propTypes = {
        cookies: instanceOf(Cookies).isRequired
      };

    constructor(props){
        super(props);

        const {cookies} = props;
        this.myCookies = new Cookies()

        this.state={
            matricola_studente: cookies.get('matricola_studente') || '',
            matricola_docente: cookies.get('matricola_docente') || '',
            password_studente: cookies.get('password_studente') || '',
            password_docente: cookies.get('password_docente') || '',
        }
    }

    login = async() => {
        let response;
        let userType;
        let isAuth;

        try{
            response = await myUniversity.post('/student/login', {
                matricola_studente: this.state.matricola_studente,
                password_studente: this.state.password_studente
            });
        }catch(error){
            console.log(`😱 There was an error: ${error}`);
            isAuth = false;
        }
        if (response.data.length !== 0){
            isAuth = true;
            userType = 'student';
        }else{
            try{
                response = await myUniversity.post('/professor/login',{
                    matricola_docente: this.state.matricola_docente,
                    password_docente: this.state.password_docente
                });
            }catch(error){
                console.log(`😱 There was an error: ${error}`);
                isAuth = false;
            }

            if (response.data.length !== 0){
                isAuth = true;
                userType = 'teacher';
            }else{
               isAuth = false;
            }
        }

        // UPDATE STATE
        this.setState({userType: userType, response:response.data[0]});
        //UPDATE COOKIES
        this.myCookies.set('isAuth',isAuth,{ path: '/' });
        //UPDATE CONTEXT
        this.context.update({[userType]:response.data[0]});
    }

    componentDidMount(){
        console.log('did mount')
        if((this.state.matricola_studente && this.state.password_studente) || 
           (this.state.matricola_docente && this.state.password_docente)){
               this.login();
           }else{
                this.myCookies.set('isAuth',false,{ path: '/' });
           }
    }

    render(){
        return (
            <div>
                <Switch>
                <AppRoute name="News" path="/" navBar={MyUniversityNav} component={News} {...this.props} exact>
                            {(this.myCookies.get('isAuth') === 'false' || this.myCookies.get('isAuth') === undefined) 
                            && <Redirect to={{pathname: "/login"}}/>}
                        </AppRoute>
                        <AppRoute name="Calendario" path="/calendario" navBar={MyUniversityNav} component={Calendar} {...this.props} exact>
                            {(this.myCookies.get('isAuth') === 'false' || this.myCookies.get('isAuth') === undefined) 
                            && <Redirect to={{pathname: "/login"}}/>}
                        </AppRoute>
                        <AppRoute name="Ricevimento" path="/ricevimento" navBar={MyUniversityNav} component={Receipt} {...this.props} exact>
                            {(this.myCookies.get('isAuth') === 'false' || this.myCookies.get('isAuth') === undefined) 
                            && <Redirect to={{pathname: "/login"}}/>}
                        </AppRoute>
                        <AppRoute name="Chat" path="/chat" navBar={MyUniversityNav} component={Chat} {...this.props} exact>
                            {(this.myCookies.get('isAuth') === 'false' || this.myCookies.get('isAuth') === undefined) 
                            && <Redirect to={{pathname: "/login"}}/>}
                        </AppRoute>
                        <AppRoute name="Profilo" path="/profilo" navBar={MyUniversityNav} component={Profile} {...this.props} exact>
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

Routes.contextType = UserContext; 

//export a component 
export default withCookies(Routes);