//import lib
import React, {Component} from 'react'
//FORM
import FormGroup from '../bootstrap/form/FormGroup';
import Submit from '../bootstrap/form/Submit';
//FORM-FIELDS
import TextField from '../bootstrap/form/fields/TextField';
import PasswordField from '../bootstrap/form/fields/PasswordField';
//API
import myUniversity from '../../API/myUniversity';

//create a component 
class LoginForm extends Component{

    constructor(props){
        super(props);

        this.state = {
            freshman: '',
            password: '',
            loginError: false
        }
    }

    onChangeFields = (event) => {
        this.setState({[event.target.name]:event.target.value});
    }

    onSubmit = async(event) => {
        event.preventDefault();

        let response;
        try{
            response = await myUniversity.post('/student/login', {
                matricola_studente: this.state.freshman,
                password_studente: this.state.password
            });
        }catch(error){
            console.log(`😱 There was an error: ${error}`);
        }

        if (response.data.length === 0){
            try{
                response = await myUniversity.post('/professor/login',{
                    matricola_docente: this.state.freshman,
                    password_docente: this.state.password
                });
            }catch(error){
                console.log(`😱 There was an error: ${error}`);
            }
        }

        if (response.data.length === 0){
            this.setState({loginError: true})
        }
    }

    render(){
        const errorMessage = !this.state.loginError ? '' : <p className='text-danger'>Matricola o password errate</p>

        return(
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
        );
    }
}

//export a component
export default LoginForm;