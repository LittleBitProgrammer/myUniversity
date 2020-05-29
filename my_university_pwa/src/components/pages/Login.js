//IMPORT LIB
import React, {Component} from 'react';
//COOKIE
import {Cookies} from 'react-cookie';
//FORM
import LoginForm from '../form/LoginForm';
//API
import myUniversity from '../../API/myUniversity';
import { Redirect } from 'react-router-dom';
//CONTEXT
import {UserContext} from '../context/UserContext';


//create a component 
class Login extends Component{

    constructor(props){
        super(props);

        this.cookies = new Cookies();

        this.state = {
            loginError: false
        }
    }

    onSubmit = async(event,freshman,password) => {
        event.preventDefault();

        let response;
        let isAuth;
        let userType;
        let thereIsAnError;

        try{
            response = await myUniversity.post('/student/login', {
                matricola_studente: freshman,
                password_studente: password
            });
        }catch(error){
            console.log(`😱 There was an error: ${error}`);
            thereIsAnError = true;
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
                thereIsAnError = true;
                isAuth = false
            }

            if (response.data.length !== 0){
                this.cookies.set('matricola_docente', freshman);
                this.cookies.set('password_docente', password);
                userType='teacher';
                isAuth = true
            }else{
                thereIsAnError = true;
                isAuth = false
            }
        }

        //UPDATE COOKIE
        this.cookies.set('isAuth',isAuth,{path:'/'});
        //UPDATE STATE
        this.setState({loginError: thereIsAnError});
        //UPDATE CONTEXT
        this.context.update({[userType]:response.data[0]});
    }

    render(){
        const errorMessage = !this.state.loginError ? '' : <p className='text-danger'>Matricola o password errate</p>

        if(this.cookies.get('isAuth') === 'false'){return(
            <div>
                <LoginForm onSubmit={this.onSubmit} error={errorMessage}/>
            </div>
        )}
        
        return  <Redirect to={{pathname: "/"}}/>
    }
}

Login.contextType = UserContext;

//export a component 
export default Login;