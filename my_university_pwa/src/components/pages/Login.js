//import lib
import React, {Component} from 'react';
//FORM
import FormGroup from '../bootstrap/form/FormGroup';
import Submit from '../bootstrap/form/Submit';
//FORM-FIELDS
import TextField from '../bootstrap/form/fields/TextField';
import PasswordField from '../bootstrap/form/fields/PasswordField';

//create a component 
class Login extends Component {
    constructor(props){
        super(props)

        this.state = {
            
        };
    }

    render(){
        return(
            <div>
                <form>
                    <h3>Login</h3>
                    <FormGroup>
                        <TextField/>
                    </FormGroup>
                    <FormGroup>
                        <PasswordField/>
                    </FormGroup>
                    <Submit classColor='btn-primary'/>
                </form>
            </div>
        );
    }
}

//export a component 
export default Login;