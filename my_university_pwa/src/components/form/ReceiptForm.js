// IMPORT LIB
import React, { Component } from 'react';
// IMPORT TEXT
import TextField from '../bootstrap/form/fields/TextField';
// IMPORT BUTTON
import Button from '../bootstrap/Button';


// CREATE A COMPONENT
class ReceiptForm extends Component{
    constructor(props){
        super(props);

        this.state = {
            inputText: ''
        }
    }

    onChange = (event) => {
        this.setState({
            inputText: event.target.value
        })
    }
    
    render(){
        console.log(this.state)
        return(
            <form>
                <div >
                    <TextField placeholder='Matricola, Es. 0124001910'/>
                    <input 
                        type='text' 
                        className='form-control form-control-lg mt-3' 
                        placeholder='Motivazione, Es."Spiegazione generatore di grafi"' 
                        onChange={this.onChange} 
                        value={this.state.inputText}/>
                    <Button classColor='btn-primary' className='mt-1 btn-right mr-0' buttontext='Invia'/>
                </div>
            </form>
        );
    }
}
// EXPORT A COMPONENT
export default ReceiptForm