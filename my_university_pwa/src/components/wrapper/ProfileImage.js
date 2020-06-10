//IMPORT LIB
import React from 'react'
//BOOTSTRAP
import RoundedImage from '../bootstrap/RoundedImage';

// CREATE A COMPONENT
const ProfileImage = ({path,altText,sigle,className,containerClass}) => {
    return (
        <div className={`img-container mt-0${containerClass?' '+containerClass:''}`}>
            <RoundedImage className={className} path={path} altText={altText} alt='profile img'/>
            <h2>{sigle}</h2>
        </div>
    );
}

// SET DEFAULT PROPS
ProfileImage.defaultProps ={
    inputText: 'Change Photo',
    altText: 'Profile Image',
    sigle: 'AB',
}

// EXPORT A COMPONENT
export default ProfileImage;