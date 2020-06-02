// IMPORT LIB
import React from 'react'
// TABBAR
import TabBar from '../../bootstrap/navigation/TabBar';
import NavTab from '../../bootstrap/navigation/NavTab';
import Row from '../../bootstrap/Row';

// CREATE A COMPONENT
const ProfileTab = (props) => {
    return (
        <div>
        <TabBar>
            <NavTab isActive={true} id='home-tab' to='home' tabName='Informazioni'/>
            <NavTab isActive={false} id='other-tab' to='other' tabName='Altro'/>
        </TabBar>
        <div className="tab-content profile-tab" id="myTabContent">
                <div className="tab-pane fade show active" id="home" role="tabpanel" aria-labelledby="home-tab">
                    <div className='profile-tab-block'>
                    <Row>
                        <div className="col-md-6">
                            <label>Matricola</label>
                        </div>
                        <div className="col-md-6">
                            <p>test</p>
                        </div>
                    </Row>
                    <Row>
                        <div className="col-md-6">
                            <label>Codice Fiscale</label>
                        </div>
                        <div className="col-md-6">
                            <p>test</p>
                        </div>
                    </Row>
                    <Row>
                        <div className="col-md-6">
                            <label>Email universitaria</label>
                        </div>
                        <div className="col-md-6">
                            <p>test</p>
                        </div>
                    </Row>
                    <Row>
                        <div className="col-md-6">
                            <label>Data Di Immatricolazione</label>
                        </div>
                        <div className="col-md-6">
                            <p>test</p>
                        </div>
                    </Row>
                </div>
                </div>
                <div className="tab-pane fade" id="other" role="tabpanel" aria-labelledby="other-tab">
                <div className='profile-tab-block'>
                    <Row>
                        <div className="col-md-6">
                            <label>Domicilio</label>
                        </div>
                        <div className="col-md-6">
                            <p>test</p>
                        </div>
                    </Row>
                    <Row>
                        <div className="col-md-6">
                            <label>Data di nascita</label>
                        </div>
                        <div className="col-md-6">
                            <p>test</p>
                        </div>
                    </Row>
                    <Row>
                        <div className="col-md-6">
                            <label>Luogo di Nascita</label>
                        </div>
                        <div className="col-md-6">
                            <p>test</p>
                        </div>
                    </Row>
                </div>
            </div>
        </div>
        </div>
    );
}

// EXPORT A COMPONENT
export default ProfileTab