// IMPORT LIB
import React, {Component} from 'react';
// GRID COMPONENT
import Row from '../../bootstrap/Row';
import Column from '../../bootstrap/Column';
// WRAPPER
import Sidebar from './Sidebar';
import ProfileImage from '../ProfileImage';
import Contacts from './Contacts';
import ProfileBody from './ProfileBody';
import ProfileHeader from './ProfileHeader';
//CONTEXT
import {UserContext} from '../../context/UserContext';
//IMAGE
import squareLogo from '../../../img/svg/Square-profile.svg'
//CSS
import '../../../css/profile.css'
import ProfileTab from '../../navmenu/tabBar/ProfileTab';


//TODO: dynamic alt text
//TODO: fix image size on smaller screen
//TODO: teacher content
//TODO: show user datetime format
//TODO: conditional rendering on profile image 
//TODO: dynamic contacts

// CREATE A COMPONENT
class ProfileInformation extends Component {
    // CLASS CONSTRUCTOR
    constructor(props){
        super(props)

        this.state = {
            // insert information here
        }
    }

    //RENDER METHOD
    render(){
        const user = this.context;
        console.log(user)
        return(
            <div>
                <Row>
                    <Column columnSize='4' screenSize='lg'>
                        <Sidebar>
                            <ProfileImage 
                              inputText='Cambia Foto' 
                              altText='Immagine del profilo' 
                              sigle= {`${user.student.nome.charAt(0).toUpperCase()} 
                                       ${user.student.cognome.charAt(0).toUpperCase()}`} 
                              path={squareLogo}/>
                              <Contacts 
                                phoneNumbers={['081233483440','081233483441','081233483442']}
                                emails={['bob@mail.it', 'bobbetto@mail.it', 'tweb@mail.it']}
                                />
                        </Sidebar>
                    </Column>
                    <Column columnSize='8' screenSize='lg'>
                        <ProfileBody>
                            <ProfileHeader 
                              firstName={user.student.nome} 
                              lastNAme={user.student.cognome} 
                              userType='studente' 
                              userYear={user.student.anno_in_corso}/>
                            <ProfileTab/>
                        </ProfileBody>
                    </Column>
                </Row>
            </div>
        );
    }
}

{/* <div>
<form>
    <Row>
        <div className="col-md-8">
            <div className="tab-content profile-tab" id="myTabContent">
                <div className="tab-pane fade show active" id="home" role="tabpanel" aria-labelledby="home-tab">
                    <div className='profile-tab-block'>
                    <Row>
                        <div className="col-md-6">
                            <label>Matricola</label>
                        </div>
                        <div className="col-md-6">
                            <p>{user.student.matricola_studente}</p>
                        </div>
                    </Row>
                    <Row>
                        <div className="col-md-6">
                            <label>Codice Fiscale</label>
                        </div>
                        <div className="col-md-6">
                            <p>{user.student.cf.toUpperCase()}</p>
                        </div>
                    </Row>
                    <Row>
                        <div className="col-md-6">
                            <label>Email universitaria</label>
                        </div>
                        <div className="col-md-6">
                            <p>{user.student.email_studente}</p>
                        </div>
                    </Row>
                    <Row>
                        <div className="col-md-6">
                            <label>Data Di Immatricolazione</label>
                        </div>
                        <div className="col-md-6">
                            <p>{user.student.data_immatricolazione}</p>
                        </div>
                    </Row>
                </div>
                </div>
                <div className="tab-pane fade" id="profile" role="tabpanel" aria-labelledby="profile-tab">
                <div className='profile-tab-block'>
                    <Row>
                        <div className="col-md-6">
                            <label>Domicilio</label>
                        </div>
                        <div className="col-md-6">
                            <p>{`Via ${user.student.via_piazza}, ${user.student.civico} - ${user.student.cap}`}</p>
                        </div>
                    </Row>
                    <Row>
                        <div className="col-md-6">
                            <label>Data di nascita</label>
                        </div>
                        <div className="col-md-6">
                            <p>{user.student.data_di_nascita}</p>
                        </div>
                    </Row>
                    <Row>
                        <div className="col-md-6">
                            <label>Luogo di Nascita</label>
                        </div>
                        <div className="col-md-6">
                            <p>{user.student.luogo_di_nascita}</p>
                        </div>
                    </Row>
                </div>
            </div>
        </div>
        </div>
    </Row>
</form>           
</div> */}

//DEFINE CONTEXT OF THE CLASS
ProfileInformation.contextType = UserContext;

// EXPORT A COMPONENT
export default ProfileInformation;