//IMPORT LIB
import React from 'react';
//FUNCTIONS
import {capitalizeFirstLetter} from '../../../utility/functions';
// GRID
import Row from '../../bootstrap/Row';
import Column from '../../bootstrap/Column';

//CREATE A COMPONENT 
const ProfileHeader = ({firstName, lastNAme, userType, userYear}) => {
    return (
        <div className="profile-head">
            <Row className='no-gutters'>
                <Column columnSize='6'>
                    <h5>
                        {`${capitalizeFirstLetter(firstName)} ${capitalizeFirstLetter(lastNAme)}`} 
                    </h5>
                    <h6>{userType}</h6>
                </Column>
                <Column columnSize='6'>
                    <p className="proile-year float-right">Anno in corso : <span className='ml-1'>{userYear}</span></p>
                </Column>
                
                
            </Row>
        </div>
    );
}

// EXPORT A COMPONENT 
export default ProfileHeader;