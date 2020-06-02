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
const ProfileTab = (props) => {
    return (
        <TabBar>
            <TabHeader>
                <NavTab isActive={true} id='home-tab' to='home' tabName='Informazioni'/>
                <NavTab isActive={false} id='other-tab' to='other' tabName='Altro'/>
            </TabHeader>
            <TabBody>
                <TabView animaationClass='fade' id='home' isActive='active show'>
                    <TabRow title='Matricola' attribute='Test1'/>
                    <TabRow title='Codice Fiscale' attribute='Test2'/>
                    <TabRow title='Email Universitaria' attribute='Test3'/>
                    <TabRow title='Data di immatricolazione' attribute='Test4'/>
                </TabView>
                <TabView animaationClass='fade' id='other'>
                    <TabRow title='Domicilio' attribute='Test1'/>
                    <TabRow title='Data di nascita' attribute='Test2'/>
                    <TabRow title='Luogo di nascita' attribute='Test3'/>
                </TabView>
            </TabBody>
        </TabBar>
    );
}

// EXPORT A COMPONENT
export default ProfileTab