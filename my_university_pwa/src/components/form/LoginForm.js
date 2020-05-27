//import lib
import React, {Component} from 'react'
//FORM
import FormGroup from '../bootstrap/form/FormGroup';
import Submit from '../bootstrap/form/Submit';
//FORM-FIELDS
import TextField from '../bootstrap/form/fields/TextField';
import PasswordField from '../bootstrap/form/fields/PasswordField';

//create a component 
class LoginForm extends Component{

    constructor(props){
        super(props);

        this.state = {
            freshman: '',
            password: ''
        }
    }

    onChangeFields = (event) => {
        this.setState({[event.target.name]:event.target.value});
    }

    render(){
        return(
            <form>
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
                <Submit classColor='btn-primary'/>
            </form>
        );
    }
}

//export a component
export default LoginForm;