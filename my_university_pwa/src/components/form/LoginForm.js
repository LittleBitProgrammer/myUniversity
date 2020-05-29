//import lib
import React, {Component} from 'react'
//ROUTER
import {Redirect} from 'react-router';
//FORM
import FormGroup from '../bootstrap/form/FormGroup';
import Submit from '../bootstrap/form/Submit';
//FORM-FIELDS
import TextField from '../bootstrap/form/fields/TextField';
import PasswordField from '../bootstrap/form/fields/PasswordField';
//API
import myUniversity from '../../API/myUniversity';
import {Cookies} from 'react-cookie';
//CONTEXT
import {UserContext} from '../context/UserContext';

//create a component 
//TODO: OPTIMIZE CALL (SPINNER)
//TODO: FIX ON RELOAD
//TODO: MOVE LOGIC IN LOGIN
class LoginForm extends Component{

    constructor(props){
        super(props);

        this.cookies = new Cookies();
        this._mount = true;

        this.state = {
            freshman: '',
            password: '',
            loginError: false,
            isAuth: this.cookies.get('isAuth') || false,
        }
    }

    onChangeFields = (event) => {
        this.setState({[event.target.name]:event.target.value});
    }

    onSubmit = async(event) => {
        event.preventDefault();

        let response;
        let isAuth;
        let userType;
        let thereIsAnError;

        try{
            response = await myUniversity.post('/student/login', {
                matricola_studente: this.state.freshman,
                password_studente: this.state.password
            });
        }catch(error){
            console.log(`😱 There was an error: ${error}`);
            thereIsAnError = true;
            isAuth = false;
        }
        if(response.data.length !== 0){
            this.cookies.set('matricola_studente', this.state.freshman);
            this.cookies.set('password_studente',this.state.password);
            userType = 'student';
            isAuth = true;
        }else{
            try{
                response = await myUniversity.post('/professor/login',{
                    matricola_docente: this.state.freshman,
                    password_docente: this.state.password
                });
            }catch(error){
                console.log(`😱 There was an error: ${error}`);
                thereIsAnError = true;
                isAuth = false
            }

            if (response.data.length !== 0){
                this.cookies.set('matricola_docente', this.state.freshman);
                this.cookies.set('password_docente',this.state.password);
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
        this.setState({isAuth: isAuth });
        this._mount && this.setState({loginError: thereIsAnError});
        //UPDATE CONTEXT
        this.context.update({[userType]:response.data[0]});
    }

    componentWillUnmount(){
        this._mount = false;
    }

    render(){
        const errorMessage = !this.state.loginError ? '' : <p className='text-danger'>Matricola o password errate</p>

        if(!this.myCookies.get('isAuth')){return  <Redirect to={{pathname: "/login"}}/>}
        return (
            <div>
                <form onSubmit={this.onSubmit}>
                    <h3>Login</h3>
                    <FormGroup>
                        <TextField
                        id='freshman'
                        name='freshman'
                        value={this.state.freshman}
                        onChange={this.onChangeFields}
                        placeholder='Matricola - Es. 0124002020'
                        required={true}
                        />
                    </FormGroup>
                    <FormGroup>
                        <PasswordField
                        id='password'
                        name='password'
                        value={this.state.password}
                        onChange={this.onChangeFields}
                        placeholder='Password'
                        required={true}
                        />
                    </FormGroup>
                    {errorMessage}
                    <Submit classColor='btn-primary'/>
                </form>
            </div>
        )
    }
}

LoginForm.contextType = UserContext;

//export a component
export default LoginForm;