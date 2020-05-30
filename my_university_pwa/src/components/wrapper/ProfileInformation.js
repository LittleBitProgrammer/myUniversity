// IMPORT LIB
import React, {Component} from 'react';
// GRID COMPONENT
import Row from '../bootstrap/Row';
import Column from '../bootstrap/Column';
//BOOTSTRAP
import Container from '../bootstrap/Container';
//CONTEXT
import {UserContext} from '../context/UserContext';
//FUNCTIONS
import {capitalizeFirstLetter} from '../../Utility/functions';

//TODO: dynamic alt text
//TODO: fix image size on smaller screen
//TODO: teacher content
//TODO: dynamic background image
//TODO: show user datetime format

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
        console.log(user);
        return(
            <div>
            <form>
                <div className="row">
                    <div className="col-md-4">
                        <div className="profile-img">
                            <div className='container-profile'>
                            <img src="data:image/jpeg;base64,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" alt="" className='rounded'/>
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
                </div>
                <div className="row">
                    <div className="col-md-4">
                        <div className="profile-work">
                            <p>Contatti Telefonici</p>
                            {/* Inserire qui contatti telefonici*/}
                            <p>Email</p>
                            {/* Inserire qui contatti email*/}
                        </div>
                    </div>
                    <div className="col-md-8">
                        <div className="tab-content profile-tab" id="myTabContent">
                            <div className="tab-pane fade show active" id="home" role="tabpanel" aria-labelledby="home-tab">
                                <div className="row">
                                    <div className="col-md-6">
                                        <label>Matricola</label>
                                    </div>
                                    <div className="col-md-6">
                                        <p>{user.student.matricola_studente}</p>
                                    </div>
                                </div>
                                <div className="row">
                                    <div className="col-md-6">
                                        <label>Codice Fiscale</label>
                                    </div>
                                    <div className="col-md-6">
                                        <p>{user.student.cf.toUpperCase()}</p>
                                    </div>
                                </div>
                                <div className="row">
                                    <div className="col-md-6">
                                        <label>Email universitaria</label>
                                    </div>
                                    <div class="col-md-6">
                                        <p>{user.student.email_studente}</p>
                                    </div>
                                </div>
                                <div className="row">
                                    <div className="col-md-6">
                                        <label>Data Di Immatricolazione</label>
                                    </div>
                                    <div className="col-md-6">
                                        <p>{user.student.data_immatricolazione}</p>
                                    </div>
                                </div>
                            </div>
                            <div className="tab-pane fade" id="profile" role="tabpanel" aria-labelledby="profile-tab">
                                <div className="row">
                                    <div className="col-md-6">
                                        <label>Domicilio</label>
                                    </div>
                                    <div className="col-md-6">
                                        <p>{`Via ${user.student.via_piazza}, ${user.student.civico} - ${user.student.cap}`}</p>
                                    </div>
                                </div>
                                <div className="row">
                                    <div className="col-md-6">
                                        <label>Data di nascita</label>
                                    </div>
                                    <div className="col-md-6">
                                        <p>{user.student.data_di_nascita}</p>
                                    </div>
                                </div>
                                <div className="row">
                                    <div className="col-md-6">
                                        <label>Luogo di Nascita</label>
                                    </div>
                                    <div className="col-md-6">
                                        <p>{user.student.luogo_di_nascita}</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </form>           
        </div>
        );
    }
}

//DEFINE CONTEXT OF THE CLASS
ProfileInformation.contextType = UserContext;

// EXPORT A COMPONENT
export default ProfileInformation;