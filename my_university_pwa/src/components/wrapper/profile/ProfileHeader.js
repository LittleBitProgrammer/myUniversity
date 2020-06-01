//IMPORT LIB
import React from 'react';
//FUNCTIONS
import {capitalizeFirstLetter} from '../../../Utility/functions';

//CREATE A COMPONENT 
const ProfileHeader = ({firstName, lastNAme, userType, userYear}) => {
    return (
        <div className="profile-head">
                <h5>
                    {`${capitalizeFirstLetter(firstName)} ${capitalizeFirstLetter(lastNAme)}`} 
                </h5>
                <h6>{userType}</h6>
                <p className="proile-year">Anno in corso : <span>{userYear}</span></p>
        </div>
    );
}

// EXPORT A COMPONENT 
export default ProfileHeader;