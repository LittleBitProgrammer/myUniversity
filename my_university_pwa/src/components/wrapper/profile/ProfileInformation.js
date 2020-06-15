// IMPORT LIB
import React from 'react';
// GRID COMPONENT
import Row from '../../bootstrap/Row';
import Column from '../../bootstrap/Column';
// WRAPPER
import Contacts from './Contacts';
import ProfileHeader from './ProfileHeader';
//CSS
import '../../../css/profile.css'
import ProfileTab from '../../navmenu/tabBar/ProfileTab';
import Card from '../../bootstrap/Card/Card';

// CREATE A COMPONENT
const ProfileInformation = ({sigle,phoneNumbers,emails,firstName,lastNAme,userYear,freshman,fCode, uEmail, uSubscription,
                             domicile,bornDate,bornPlace}) => {
    return(
        <div className='profile'>
            <Row className='no-gutters'>
                <Column columnSize='12'>
                    <ProfileHeader 
                        firstName={firstName} 
                        lastNAme={lastNAme} 
                        userType='studente' 
                        userYear={userYear}/>
                    <Card className='border-warning'>
                        <ProfileTab
                            freshman={freshman}
                            fCode={fCode}
                            uEmail={uEmail}
                            uSubscription={uSubscription}
                            domicile={domicile}
                            bornDate={bornDate}
                            bornPlace={bornPlace}/>
                    </Card>
                    <hr/>
                    <Contacts 
                        phoneNumbers={phoneNumbers}
                        emails={emails}
                        />
                </Column>
            </Row>
        </div>
    );
}

// EXPORT A COMPONENT
export default ProfileInformation;