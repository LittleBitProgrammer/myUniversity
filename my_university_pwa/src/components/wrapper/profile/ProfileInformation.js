// IMPORT LIB
import React, {Component} from 'react';
// GRID COMPONENT
import Row from '../../bootstrap/Row';
import Column from '../../bootstrap/Column';
// WRAPPER
import Sidebar from './Sidebar';
//CONTEXT
import {UserContext} from '../../context/UserContext';
//FUNCTIONS
import {capitalizeFirstLetter} from '../../../Utility/functions';
//IMAGE
import squareLogo from '../../../img/svg/Square-profile.svg'
//CSS
import '../../../css/profile.css'

//TODO: dynamic alt text
//TODO: fix image size on smaller screen
//TODO: teacher content
//TODO: show user datetime format
//TODO: conditional rendering on profile image 

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
        return(
            <div>
                <Row>
                    <Column columnSize='3'>
                        <Sidebar>
                            
                        </Sidebar>
                    </Column>
                    <Column columnSize='9'>
                        ciao mondo
                    </Column>
                </Row>
            </div>
        );
    }
}

{/* <div>
<form>
    <Row>
        <div className="col-md-4">
            <div className="profile-img">
                <div className='container-profile'>
                <img src={squareLogo} alt="" className='rounded'/>
                <div className="profile-sigle">
                    {`${user.student.nome.charAt(0).toUpperCase()} ${user.student.cognome.charAt(0).toUpperCase()}`}
                </div>
                <div className="file btn btn-lg btn-primary text-block">
                    Cambia Foto
                    <input type="file" name="file"/>
                </div>
                </div>
            </div>
        </div>
        <div className="col-md-6">
            <div className="profile-head">
                <h5>
                    {`${capitalizeFirstLetter(user.student.nome)} ${capitalizeFirstLetter(user.student.cognome)}`} 
                </h5>
                <h6>Studente</h6>
                <p className="proile-year">Anno in corso : <span>{user.student.anno_in_corso}</span></p>
                <ul className="nav nav-tabs" id="myTab" role="tablist">
                    <li className="nav-item">
                        <a className="nav-link active" id="home-tab" data-toggle="tab" href="#home" role="tab" aria-controls="home" aria-selected="true">Informazioni</a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-link" id="profile-tab" data-toggle="tab" href="#profile" role="tab" aria-controls="profile" aria-selected="false">Altro</a>
                    </li>
                </ul>
            </div>
        </div>
    </Row>
    <Row>
        <div className="col-md-4">
            <div className="profile-work">
                <p>Contatti Telefonici</p>
                <p>Email</p>
            </div>
        </div>
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