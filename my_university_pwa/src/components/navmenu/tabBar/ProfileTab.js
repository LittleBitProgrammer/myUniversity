// IMPORT LIB
import React from 'react'
// TABBAR
import TabBar from '../../bootstrap/navigation/TabBar';
import NavTab from '../../bootstrap/navigation/NavTab';
import TabHeader from '../../bootstrap/navigation/TabHeader';
import TabBody from '../../bootstrap/navigation/TabBody';
import TabView from '../../bootstrap/navigation/TabView';
import TabRow from '../../bootstrap/navigation/TabRow';

// CREATE A COMPONENT
const ProfileTab = ({freshman,fCode,uEmail,uSubscription,domicile,bornDate,bornPlace}) => {
    return (
        <TabBar className='mt-4'>
            <TabHeader>
                <NavTab isActive={true} id='home-tab' to='home' tabName='Informazioni'/>
                <NavTab isActive={false} id='other-tab' to='other' tabName='Altro'/>
            </TabHeader>
            <TabBody className='mt-4'>
                <TabView animaationClass='fade' id='home' isActive='active show' className='profile-tab'>
                    <TabRow title='Matricola' attribute={freshman}/>
                    <TabRow title='Codice Fiscale' attribute={fCode}/>
                    <TabRow title='Email Universitaria' attribute={uEmail}/>
                    <TabRow title='Data di immatricolazione' attribute={uSubscription}/>
                </TabView>
                <TabView animaationClass='fade' id='other' className='profile-tab'>
                    <TabRow title='Domicilio' attribute={domicile}/>
                    <TabRow title='Data di nascita' attribute={bornDate}/>
                    <TabRow title='Luogo di nascita' attribute={bornPlace}/>
                </TabView>
            </TabBody>
        </TabBar>
    );
}

// EXPORT A COMPONENT
export default ProfileTab