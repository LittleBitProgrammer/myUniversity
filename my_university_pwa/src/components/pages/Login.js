//IMPORT LIB
import React, {Component} from 'react';
//COOKIE
import {Cookies} from 'react-cookie';
//FORM
import LoginForm from '../form/LoginForm';
//ERROR
import CardError from '../error/CardError';
//API
import myUniversity from '../../API/myUniversity';
import { Redirect } from 'react-router-dom';
//CONTEXT
import {UserContext} from '../context/UserContext';
// CSS
import '../../css/login.css';

//TODO: cookie banner showed to the user

//create a component 
class Login extends Component{

    constructor(props){
        super(props);

        // THIS PAGE USE COOKIES TO MEMORIZE IN IT PASSWORD AND FRESHMAN,
        // USED TO AUTOMATIC LOGIN THE USER ON THE NEXT LOGIN
        this.cookies = new Cookies();

        // THE STATE MEMORIZE EVENTUALLY ERRORS
        this.state = {
            loginError: false
        }
    }

    // CALLED ON SUBMIT LOGIN FORM
    onSubmit = async(event,freshman,password) => {
        // PREVENT THE DEFAULT ACTION INJECTED BY  THE BROSWER WHEN THE FORM IS SUBMIT
        event.preventDefault();

        // TEMP VARIABLES USED TO TAKE RESPONSE, AUTHENTICATION AND USER TYPE
        let response;
        let isAuth;
        let userType;

        //LOGIN CALL
        try{
            response = await myUniversity.post('/student/login', {
                matricola_studente: freshman,
                password_studente: password
            });
        }catch(error){
            console.log(`😱 There was an error: ${error}`);
            this.setState({loginError: true});
            isAuth = false;
        }
        if(response.data.length !== 0){
            this.cookies.set('matricola_studente', freshman);
            this.cookies.set('password_studente',password);
            userType = 'student';
            isAuth = true;
        }else{
            try{
                response = await myUniversity.post('/professor/login',{
                    matricola_docente: freshman,
                    password_docente: password
                });
            }catch(error){
                console.log(`😱 There was an error: ${error}`);
                this.setState({loginError: true});
                isAuth = false
            }

            if (response.data.length !== 0){
                this.cookies.set('matricola_docente', freshman);
                this.cookies.set('password_docente', password);
                userType='teacher';
                isAuth = true
            }else{
                this.setState({loginError: true});
                isAuth = false
            }
        }

        //UPDATE COOKIE
        this.cookies.set('isAuth',isAuth,{path:'/'});
        this.cookies.set('userCookies', response.data[0] );

        //UPDATE CONTEXT
        this.context.update({[userType]:response.data[0], isAuth: !this.context.isAuth});
    }

    //RENDER METHOD
    render(){
        // CONTROL IF THE ERROR IS PRESENT 
        console.log(this.cookies.get('isAuth'));
        const errorMessage = !this.state.loginError ? '' : <CardError errorMessage='Matricola o password errate'/>
        if(this.cookies.get('isAuth') === 'true'){console.log('from redirect',this.cookies.get('isAuth'));return  <Redirect to='/' key='login-to-root'/>}
        return(
                <div>
                    <LoginForm onSubmit={this.onSubmit} error={errorMessage}/>
                </div>
            )
    }
}

Login.contextType = UserContext;

//export a component 
export default Login;