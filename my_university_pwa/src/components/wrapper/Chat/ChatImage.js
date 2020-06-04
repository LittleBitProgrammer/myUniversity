//IMPORT LIB
import React from 'react'
//BOOTSTRAP
import RoundedImage from '../../bootstrap/RoundedImage';

// CREATE A COMPONENT
const ChatImg = ({path,altText ,sigle ,className}) => {
    return (
        <div className={`${className? className: null}`}>
            <div>
                <RoundedImage path={path} alt={altText}/>
                <div className="profile-sigle">
                    {sigle}
                </div>
            </div>
        </div>
    );
}

// SET DEFAULT PROPS
ChatImg.defaultProps ={
    altText: 'Profile Image',
    sigle: 'AB'
}

// EXPORT A COMPONENT
export default ChatImg;