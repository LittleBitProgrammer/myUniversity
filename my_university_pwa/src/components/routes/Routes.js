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
import AppRoute from '../AppRoute';
// NAVBAR
import MyUniversityNav from '../navabar/MyUniversityNav'
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
            isAuth: cookies.get('isAuth') || false,
        }
    }

    login = async() => {
        let response;
        let userType;
        //console.log('login',this.state.matricola_studente, this.state.password_studente)
        try{
            response = await myUniversity.post('/student/login', {
                matricola_studente: this.state.matricola_studente,
                password_studente: this.state.password_studente
            });
        }catch(error){
            console.log(`😱 There was an error: ${error}`);
            this.myCookies.set('isAuth',false,{ path: '/' });
        }
        if (response.data.length !== 0){
            this.myCookies.set('isAuth',true,{ path: '/' });
            userType = 'student';
        }else{
            try{
                response = await myUniversity.post('/professor/login',{
                    matricola_docente: this.state.matricola_docente,
                    password_docente: this.state.password_docente
                });
            }catch(error){
                console.log(`😱 There was an error: ${error}`);
                this.myCookies.set('isAuth',false,{ path: '/' });
            }

            if (response.data.length !== 0){
                this.myCookies.set('isAuth',true,{ path: '/' });
                userType = 'teacher';
            }else{
                this.myCookies.set('isAuth',false,{ path: '/' });
            }
        }

        this.setState({userType: userType, response:response.data[0]});
        this.context.update({[userType]:response.data[0]});
        console.log('home resp',this.state.response, 'home user type', this.state.userType);
    }

    componentDidMount(){
        console.log(this.state.matricola_studente,'-',this.state.password_studente,'-',this.state.matricola_docente,'-',this.state.password_docente);
        if((this.state.matricola_studente && this.state.password_studente) || 
           (this.state.matricola_docente && this.state.password_docente)){
               this.login();
           }else{
               this.setState({isAuth: false})
           }
    }

    render(){
        console.log('cookie auth',this.state.isAuth);
        return (
            <div>
                { !this.state.isAuth && <Redirect to={{pathname: "/login"}}/>}

                <Switch>
                    <AppRoute name="News" path="/" navBar={MyUniversityNav} component={News} exact/>
                    <AppRoute name="Calendario" path="/calendario" navBar={MyUniversityNav} component={Calendar}/>
                    <AppRoute name="Ricevimento" path="/ricevimento" navBar={MyUniversityNav} component={Receipt}/>
                    <AppRoute name="Chat" path="/chat" navBar={MyUniversityNav} component={Chat}/>
                    <AppRoute name="Profilo" path="/profilo" navBar={MyUniversityNav} component={Profile}/>
                    <AppRoute name="Login" path="/login"  component={Login}/>
                </Switch>
            </div>
        );
    }
}

Routes.contextType = UserContext; 

//export a component 
export default withCookies(Routes);