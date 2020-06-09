// IMPORT LIB
import React, { Component } from 'react';
// IMPORT TEXT
import TextArea from '../bootstrap/form/fields/TextArea';
// IMPORT API
import myUnversity from '../../API/myUniversity';
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
            inputText: value
        });
    }

    onSubmitForm = (event) =>{
        event.preventDefault();
        console.log(this.props.matricola_studente,
         this.props.matricola_docente,
         this.props.date,
         this.state.inputText)
        try{
            myUnversity.post('/student/richiesta_ricevimento', {
                            'matricola_docente': this.props.matricola_docente,
                            'data_ricevimento': this.props.date,
                            'matricola_studente': this.props.matricola_studente,
                            'motivazione_ricevimento': this.state.inputText})
        }catch(error){
            console.log(`There was an error: ${error}`);
        }
    }

    render(){
        console.log(this.state)
        return(
            <form onSubmit={this.onSubmitForm}>
                
                <h5>Matricola: {this.props.matricola_studente}</h5>
                <TextArea 
                    maxRows={10}
                    className='form-control form-control-lg mt-2' 
                    textCallback={this.onChange}
                    placeholder='Motivazione, Es."Spiegazione generatore di grafi"'
                    />
                <Submit classColor='btn-primary' className='mt-1 btn-right mr-0' buttontext='Invia'/>
                
            </form>
        );
    }
}
// EXPORT A COMPONENT
export default ReceiptForm