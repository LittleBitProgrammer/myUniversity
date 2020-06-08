// IMPORT LIB
import React, { Component } from 'react';
// IMPORT TEXT
import TextArea from '../bootstrap/form/fields/TextArea';
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
        console.log(this.props.matricola_studente)
        console.log(this.state)
        return(
            <form>
                <div>
                    <h5>Matricola: {this.props.matricola_studente}</h5>
                    <TextArea 
                        type='text'
                        maxRows={10}
                        className='form-control form-control-lg mt-2' 
                        onChange={this.onChange}
                        value={this.state.inputText}
                        placeholder='Motivazione, Es."Spiegazione generatore di grafi"'
                        />
                    <Button classColor='btn-primary' className='mt-1 btn-right mr-0' buttontext='Invia'/>
                </div>
            </form>
        );
    }
}
// EXPORT A COMPONENT
export default ReceiptForm