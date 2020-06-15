//IMPORT LIB
import React, {Component} from 'react'
//FORM
import FormGroup from '../bootstrap/form/FormGroup';
import Submit from '../bootstrap/form/Submit';
//FORM-FIELDS
import TextField from '../bootstrap/form/fields/TextField';
import PasswordField from '../bootstrap/form/fields/PasswordField';
//IMAGES
import myUniversityLogo from '../../img/svg/graduation-hat-primary.svg'


//create a component 
//TODO: OPTIMIZE CALL (SPINNER)
class LoginForm extends Component{

    constructor(props){
        super(props);

        // THE STATE MEMORIZE FRESHMAN AND PASSWORD
        this.state = {
            freshman: '',
            password: ''
        }
    }

    // CALLED ON INPUTS CHANGES
    onChangeFields = (event) => {
        this.setState({[event.target.name]:event.target.value});
    }

    // RENDER METHOD
    render(){
        return (
            <div className='text-center'>
                <form 
                  onSubmit={(event) => this.props.onSubmit(event,this.state.freshman,this.state.password)} 
                  className='form-signin'>
                    {/* FORM HEADING */}
                    <img className='mb-4' alt='My University Logo' src={myUniversityLogo} width='72px' height='72px'/>
                    <h1 className='h3 mb-3 font-weight-normal'>Please sign in</h1>
                    {/* FORM INPUT */}
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

                    {/* EROOR SPACE */}
                    {this.props.error}

                    {/* SUBMIT BUTTON FORM */}
                    <Submit 
                      classColor='btn-primary' 
                      className='btn-lg btn-block mt-5' 
                      buttontext='Login' 
                      isLoading={this.props.isLoading}/>
                </form>
            </div>
        )
    }
}

// EXPORT A COMPONENT
export default LoginForm;