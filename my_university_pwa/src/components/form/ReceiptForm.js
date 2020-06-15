// IMPORT LIB
import React, { Component } from 'react';
// IMPORT TEXT
import TextArea from '../bootstrap/form/fields/TextArea';
// IMPORT SUBMIT
import Submit from '../bootstrap/form/Submit';

// CREATE A COMPONENT
class ReceiptForm extends Component{
    constructor(props){
        super(props);

        this.state = {
            inputText: ''
        }
    }

    onChange = (value) => {
        this.setState({
            inputText: value,
            isError: false
        });
    }

    onSubmitForm = (event) =>{
        event.preventDefault();
        const {matricola_docente,date,matricola_studente,id} = this.props;

        if(this.state.inputText){
            this.props.onReceiptSubmit(matricola_docente,date,matricola_studente,this.state.inputText,id)
            this.setState({
                inputText: ''
            })
        }else{
            this.setState({
                isError: true
            })
        }
    }

    render(){
        return(
            <form onSubmit={this.onSubmitForm}>
                <TextArea 
                    id={this.props.id}
                    maxRows={10}
                    minRows={3}
                    textCallback={this.onChange}
                    className={`form-control form-control-lg mt-3${this.state.isError ? ' is-invalid' : ''}`}
                    placeholder='Motivazione, Es."Spiegazione generatore di grafi"'
                    inputValue={this.state.inputText}
                    />
                    <div className="invalid-feedback">
                        Inserisci una motivazione valida...
                    </div>
                <Submit classColor='btn-primary' className='btn-right w-100 mt-3' buttontext='Effettua Prenotazione'/>
            </form>
        );
    }
}
// EXPORT A COMPONENT
export default ReceiptForm