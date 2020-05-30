//IMPORT LIB
import React, {Component} from 'react';
import {UserContext} from './UserContext';

// CREATE A COMPONENT
class UserProvider extends Component {
    constructor(props){
        super(props)

        this.updateState = this.updateState.bind(this);
        this.state = {
            student:{
                cf: '',
                nome: '',
                cognome: '',
                data_di_nascita: '',
                luogo_di_nascita: '',
                cap: 0,
                via_piazza: '',
                civico: '',
                matricola_studente: '',
                email_studente: '',
                data_immatricolazione: '',
                anno_in_corso: 0,
                contatti: [
                    {
                      tipo_contatto: '',
                      valore_contatto: ''
                    }
                       ]
            },
            teacher: {
                cf: '',
                nome: '',
                cognome: '',
                data_di_nascita: '',
                luogo_di_nascita: '',
                cap: '',
                via_piazza: '',
                civico: '',
                matricola_docente: '',
                email_docente: '',
                contatti: [
                 {
                   tipo_contatto: '',
                   valore_contatto: ''
                 }
                    ]
            },
            update: this.updateState
        }
    }

    updateState(values){ 
        this.setState(values)
    }

    render() {
		return (
			<UserContext.Provider value={this.state}>
				{this.props.children}
			</UserContext.Provider>
		)
	}
}

export default UserProvider;