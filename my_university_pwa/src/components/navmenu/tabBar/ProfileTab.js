// IMPORT LIB
import React from 'react'
// TABBAR
import TabBar from '../navigation_utility/TabBar';

// CREATE A COMPONENT
const ProfileTab = (props) => {
    return (
        <TabBar>
            <li className="nav-item">
                <a className="nav-link active" id="home-tab" data-toggle="tab" href="#home" role="tab" aria-controls="home" aria-selected="true">Informazioni</a>
            </li>
            <li className="nav-item">
                <a className="nav-link" id="profile-tab" data-toggle="tab" href="#profile" role="tab" aria-controls="profile" aria-selected="false">Altro</a>
            </li>
        </TabBar>
    );
}

// EXPORT A COMPONENT
export default ProfileTab