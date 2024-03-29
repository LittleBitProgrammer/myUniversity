// IMPORT LIB
import React, {Component} from 'react';
// WRAPPER
import ProfileInformation from '../wrapper/profile/ProfileInformation';
//CONTEXT
import {UserContext} from '../context/UserContext';
// UTILITY FUNCTION
import {formatDate} from '../../utility/functions';

//CREATE A COMPONENT
class Profile extends Component{

    populateContacts = (user) => {
        const contacts = {
                phoneNumbers: [],
                emails: []
        }

        if(user.student.contatti.length !== 0){
            user.student.contatti.forEach((contatto) => {
                if(contatto.tipo_contatto === 'telefono'){
                    contacts.phoneNumbers.push(contatto.valore_contatto);
                }else{
                    contacts.emails.push(contatto.valore_contatto);
                }
            })
        }
        return contacts;
    }

    render(){
        const user = this.context;

        const contacts = this.populateContacts(user);
        return (
            <ProfileInformation 
              sigle={`${user.student.nome.charAt(0).toUpperCase()}${user.student.cognome.charAt(0).toUpperCase()}`} 
              phoneNumbers={contacts.phoneNumbers}
              emails={contacts.emails}
              firstName={user.student.nome} 
              lastNAme={user.student.cognome} 
              userYear={user.student.anno_in_corso}
              freshman={user.student.matricola_studente}
              fCode={user.student.cf}
              uEmail={user.student.email_studente}
              uSubscription={formatDate(user.student.data_immatricolazione)}
              domicile={`${user.student.via_piazza}, ${user.student.civico} - ${user.student.cap}`}
              bornDate={formatDate(user.student.data_di_nascita)}
              bornPlace={user.student.luogo_di_nascita}
            />
        )
    }
}

//DEFINE CONTEXT OF THE CLASS
Profile.contextType = UserContext;

//EXPORT A COMPONENT
export default Profile;