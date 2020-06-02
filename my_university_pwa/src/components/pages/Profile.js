// IMPORT LIB
import React, {Component} from 'react';
// WRAPPER
import ProfileInformation from '../wrapper/profile/ProfileInformation';
//CONTEXT
import {UserContext} from '../context/UserContext';

//TODO: dynamic alt text
//TODO: fix image size on smaller screen
//TODO: teacher content
//TODO: show user datetime format
//TODO: conditional rendering on profile image 
//TODO: dynamic contacts

//CREATE A COMPONENT
class Profile extends Component{

    populateContacts = (user,obj) => {
        console.log('len =', user.student.contatti.length);
        if(user.student.contatti.length !== 0){
            user.student.contatti.forEach((contatto) => {
                if(contatto.tipo_contatto === 'telefono'){
                    obj.phoneNumbers.push(contatto.valore_contatto);
                }else{
                    obj.emails.push(contatto.valore_contatto);
                }
            })
        }
    }

    contacts = {
        phoneNumbers: [],
        emails: []
    }

    render(){
        const user = this.context;
        this.populateContacts(user,this.contacts);

        console.log(user.student);
        console.log(this.contacts);
        return (
            <ProfileInformation 
              sigle={`${user.student.nome.charAt(0).toUpperCase()}${user.student.cognome.charAt(0).toUpperCase()}`} 
              phoneNumbers={this.contacts.phoneNumbers}
              emails={this.contacts.emails}
              firstName={user.student.nome} 
              lastNAme={user.student.cognome} 
              userYear={user.student.data_immatricolazione}
              freshman={user.student.matricola_studente}
              fCode={user.student.cf}
              uEmail={user.student.email_studente}
              uSubscription={user.student.data_immatricolazione}
              domicile={`${user.student.via_piazza}, ${user.student.civico} - ${user.student.cap}`}
              bornDate={user.student.data_di_nascita}
              bornPlace={user.student.luogo_di_nascita}
            />
        )
    }
}

//DEFINE CONTEXT OF THE CLASS
Profile.contextType = UserContext;

//EXPORT A COMPONENT
export default Profile;