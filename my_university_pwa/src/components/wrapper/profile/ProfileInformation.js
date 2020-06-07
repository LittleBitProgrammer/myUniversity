// IMPORT LIB
import React from 'react';
// GRID COMPONENT
import Row from '../../bootstrap/Row';
import Column from '../../bootstrap/Column';
// WRAPPER
import Sidebar from './ProfileSide';
import ProfileImage from '../ProfileImage';
import Contacts from './Contacts';
import ProfileBody from './ProfileBody';
import ProfileHeader from './ProfileHeader';
//IMAGE
import squareLogo from '../../../img/svg/Square-profile.svg'
//CSS
import '../../../css/profile.css'
import ProfileTab from '../../navmenu/tabBar/ProfileTab';

// CREATE A COMPONENT
const ProfileInformation = ({sigle,phoneNumbers,emails,firstName,lastNAme,userYear,freshman,fCode, uEmail, uSubscription,
                             domicile,bornDate,bornPlace}) => {
    return(
        <div>
            <Row>
                <Column columnSize='4' screenSize='lg'>
                    <Sidebar>
                        <ProfileImage 
                            inputText='Cambia Foto' 
                            altText='Immagine del profilo' 
                            sigle= {sigle}
                            path={squareLogo}/>
                            <Contacts 
                            phoneNumbers={phoneNumbers}
                            emails={emails}
                            />
                    </Sidebar>
                </Column>
                <Column columnSize='8' screenSize='lg'>
                    <ProfileBody>
                        <ProfileHeader 
                            firstName={firstName} 
                            lastNAme={lastNAme} 
                            userType='studente' 
                            userYear={userYear}/>
                        <ProfileTab
                            freshman={freshman}
                            fCode={fCode}
                            uEmail={uEmail}
                            uSubscription={uSubscription}
                            domicile={domicile}
                            bornDate={bornDate}
                            bornPlace={bornPlace}
                        />
                    </ProfileBody>
                </Column>
            </Row>
        </div>
    );
}

// EXPORT A COMPONENT
export default ProfileInformation;