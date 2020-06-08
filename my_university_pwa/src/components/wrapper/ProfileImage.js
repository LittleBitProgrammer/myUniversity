//IMPORT LIB
import React from 'react'
//BOOTSTRAP
import RoundedImage from '../bootstrap/RoundedImage';

// CREATE A COMPONENT
const ProfileImage = ({path,altText,sigle,inputText,isVisibleInput,className,size}) => {
    return (
        <div className="img-container">
            <RoundedImage className={className} path={path} altText={altText} height={size} width={size} alt='profile img'/>
            <h2>{sigle}</h2>
        </div>
    );
}

// SET DEFAULT PROPS
ProfileImage.defaultProps ={
    inputText: 'Change Photo',
    altText: 'Profile Image',
    sigle: 'AB',
    isVisibleInput: true
}

// EXPORT A COMPONENT
export default ProfileImage;